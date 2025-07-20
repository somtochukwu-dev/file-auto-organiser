import os
import shutil

# Folder to organize
folder_path = 'business-folder'

# Define folder categories based on file extensions
file_types = {
    'Legal': ['.pdf', '.docx'],
    'Financials': ['.pdf', '.jpg'],
    'Marketing': ['.png', '.jpg'],
    'Reports': ['.docx', '.xlsx'],
    'Communications': ['.txt', '.pdf']
}

# Create target folders if they don't exist
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Organize files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip if it's already a folder
    if os.path.isdir(file_path):
        continue

    # Check file extension and move
    _, extension = os.path.splitext(filename)
    moved = False

    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            shutil.move(file_path, os.path.join(folder_path, folder, filename))
            print(f"✅ Moved {filename} → {folder}/")
            moved = True
            break

    if not moved:
        print(f"⏭️ Skipped {filename} (no matching category)")

print("🎉 Finished organizing files!")
