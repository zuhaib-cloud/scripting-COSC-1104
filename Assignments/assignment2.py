import os
import shutil
import time

# Define the directory to organize
directory_to_organize = r"C:\Test"  # Update with your directory path

# Define the folder structure you want to create
file_type_folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def organize_files(directory):
    # Ensure each folder exists, or create it if it doesn't
    for folder_name in file_type_folders:
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Go through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files based on their extension
        file_moved = False
        for folder_name, extensions in file_type_folders.items():
            if filename.lower().endswith(tuple(extensions)):
                new_path = os.path.join(directory, folder_name, filename)
                shutil.move(file_path, new_path)
                print(f"Moved: {filename} to {folder_name} folder")
                file_moved = True
                break

        # If the file type doesn't match any folder, move it to 'Others'
        if not file_moved:
            other_folder = os.path.join(directory, "Others")
            os.makedirs(other_folder, exist_ok=True)
            new_path = os.path.join(other_folder, filename)
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} to Others folder")

def run_daily():
    while True:
        organize_files(directory_to_organize)  # Run the file organizer
        print("Waiting for the next execution...")
        time.sleep(86400)  # Sleep for 24 hours (86,400 seconds)

# Run the script every 24 hours
run_daily()
