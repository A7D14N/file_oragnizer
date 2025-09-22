import os
import shutil

# Define folder categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Other": []
}

def organize_folder(folder_path):
    """Organize files in the given folder into categorized subfolders."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break

            if not moved:  # If no category matched
                target_folder = os.path.join(folder_path, "Other")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    if os.path.isdir(folder):
        organize_folder(folder)
        print("^ u ^ Folder organized successfully!")
    else:
        print("! o ! Invalid folder path.")
