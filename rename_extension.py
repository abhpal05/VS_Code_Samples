import os

# Define the folder path and the old and new extensions
folder_path = 'C:\\\\Users\\abhij\\OneDrive\\HhH\\P'
old_extension = '.jpg'
new_extension = '.jpeg'
substring_old = '.trashed'
substring_new = ''

for filename in os.listdir(folder_path):
    # Check if the file name contains the substring to remove
    if substring_old in filename:
        # Create the new filename by replacing the unwanted part with an empty string
        new_filename = filename.replace(substring_old, substring_new)
        # Create the full paths to the old and new files
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print("file renamed from " + old_file + " to " + new_file)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file ends with the old extension
    if filename.endswith(old_extension):
        # Create the new filename by replacing the old extension with the new one
        new_filename = filename.replace(old_extension, new_extension)
        # Create the full paths to the old and new files
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print("file renamed from " + old_file + " to " + new_file)

print("All files have been renamed.")