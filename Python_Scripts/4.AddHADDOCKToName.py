import os

# Loop through all files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pdb'):
        # Split filename and extension
        base, ext = os.path.splitext(filename)
        # Construct new filename
        new_name = f"{base}_HADDOCK{ext}"
        # Rename the file
        os.rename(filename, new_name)
        print(f"Renamed: {filename} → {new_name}")
