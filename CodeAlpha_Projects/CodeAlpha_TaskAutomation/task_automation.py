import os
import shutil

print("JPG File Organizer")

folder = input("Enter folder path: ").strip()

if not os.path.exists(folder):
    print("Folder not found.")
else:
    jpg_folder = os.path.join(folder, "JPG_Files")

    if not os.path.exists(jpg_folder):
        os.mkdir(jpg_folder)

    count = 0

    for file in os.listdir(folder):

        if file.lower().endswith(".jpg"):
            old_file = os.path.join(folder, file)
            new_file = os.path.join(jpg_folder, file)

            shutil.move(old_file, new_file)

            print(file, "moved successfully.")
            count += 1

    print("\nTotal JPG files moved:", count)
    print("Task completed.")