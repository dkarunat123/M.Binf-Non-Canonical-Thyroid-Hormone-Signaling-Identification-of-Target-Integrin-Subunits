import zipfile
import os
import math
from collections import defaultdict

# Constants
R = 1.987  # cal/(mol·K)
T = 298.15  # Kelvin

# Step 1: Collect raw data from each zip
grouped = defaultdict(list)

for fname in os.listdir("."):
    if fname.endswith("_PRODIGY.zip"):
        try:
            with zipfile.ZipFile(fname, 'r') as z:
                if "output.out" in z.namelist():
                    with z.open("output.out") as f:
                        for line in f:
                            line = line.decode('utf-8').strip()

                            if (not line or line.startswith("#") or
                                line.startswith("command:") or
                                line.startswith("exit status") or
                                line.startswith("log:") or
                                "DGprediction" in line):
                                continue

                            parts = line.split()
                            if len(parts) >= 2:
                                try:
                                    dg = float(parts[1])
                                    dg_cal = dg * 1000
                                    kd = math.exp(dg_cal / (R * T))
                                    integrin = fname.split("_")[0]
                                    ligand = "_".join(fname.split("_")[1:-1])
                                    grouped[integrin].append((ligand, dg, kd))
                                    break
                                except ValueError:
                                    print(f"⚠️ Could not parse DG from {fname}: {line}")
                                    break
        except Exception as e:
            print(f"❌ Error processing {fname}: {e}")

# Step 2: Write results grouped by integrin, with internal rank
with open("ProdigyGroupedByIntegrin.txt", "w") as outfile:
    for integrin in sorted(grouped.keys()):
        entries = sorted(grouped[integrin], key=lambda x: x[1])  # sort by DG (ΔG)
        outfile.write(f"=== {integrin} ===\n")
        outfile.write("Ligand\tDGprediction_kcal_per_mol\tKd_M\tRank\n")
        rank = 1
        prev_dg = None
        for i, (ligand, dg, kd) in enumerate(entries):
            if i > 0 and dg != prev_dg:
                rank = i + 1
            prev_dg = dg
            outfile.write(f"{ligand}\t{dg}\t{kd:.3e}\t{rank}\n")
        outfile.write("\n")
