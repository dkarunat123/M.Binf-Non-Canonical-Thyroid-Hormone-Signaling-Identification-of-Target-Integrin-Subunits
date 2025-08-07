import os

# Loop through all files in the current directory
for fname in os.listdir("."):
    if fname.endswith(".zip") and not fname.endswith("_PRODIGY.zip"):
        new_name = fname[:-4] + "_PRODIGY.zip"
        os.rename(fname, new_name)
        print(f"Renamed: {fname} → {new_name}")
