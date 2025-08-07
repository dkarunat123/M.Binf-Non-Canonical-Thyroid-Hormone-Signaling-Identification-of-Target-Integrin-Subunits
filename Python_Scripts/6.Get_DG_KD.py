import zipfile
import os
import math

# Constants
R = 1.987  # cal/(mol·K)
T = 298.15  # Kelvin

results = []

for fname in os.listdir("."):
    if fname.endswith("_PRODIGY.zip"):
        try:
            with zipfile.ZipFile(fname, 'r') as z:
                if "output.out" in z.namelist():
                    with z.open("output.out") as f:
                        for line in f:
                            line = line.decode('utf-8').strip()

                            # Skip lines that are not data lines (comments, headers, commands)
                            if (
                                not line
                                or line.startswith("#")
                                or line.startswith("command:")
                                or line.startswith("exit status")
                                or line.startswith("log:")
                                or "DGprediction" in line
                            ):
                                continue

                            # Parse first valid data line
                            parts = line.split()
                            if len(parts) >= 2:
                                try:
                                    dg = float(parts[1])  # DGprediction
                                    dg_cal = dg * 1000
                                    kd = math.exp(dg_cal / (R * T))
                                    results.append((fname, dg, kd))
                                    break  # Stop after first valid data line
                                except ValueError:
                                    print(f"⚠️ Could not parse DG from {fname}: {line}")
                                    break
        except Exception as e:
            print(f"❌ Error processing {fname}: {e}")

# Step 2: Sort by DGprediction (more negative = better)
results_sorted = sorted(results, key=lambda x: x[1])

# Step 3: Assign tied ranks
ranks = []
current_rank = 1
for i, (fname, dg, kd) in enumerate(results_sorted):
    if i > 0 and dg != results_sorted[i - 1][1]:
        current_rank = i + 1
    ranks.append((fname, dg, kd, current_rank))

# Step 4: Write output
with open("ProdigyScores.txt", "w") as outfile:
    outfile.write("ZipFile\tDGprediction_kcal_per_mol\tKd_M\tRank\n")
    for fname, dg, kd, rank in ranks:
        outfile.write(f"{fname}\t{dg}\t{kd:.3e}\t{rank}\n")
