import os
import shutil
downloads_path = os.path.expanduser("~/Downloads")
print("We will organize files in:",downloads_path)
image_folder = os.path.join(downloads_path, "Images")
document_folder = os.path.join(downloads_path,"Documents")
input("Press Enter to continue...")
folders_to_create = [image_folder, document_folder]
print ("\nCreating organization folders...")
for folder_path in folders_to_create:
    os.makedirs(folder_path, exist_ok= True)
    print(f"created:{folder_path}")
print("Folder creation complete!")
input("Press Enter to continue...")
file_types = {"Images":['.jpg', '.jpeg', '.png', '.gif'],
             "Documents":['.pdf','.docx','.txt','.xlsx']}
print("n\File organization rules:")
print("-images will move to Images/folder")
print("-Documents will move to Documents/folder")
print("-other files will stay in Downloads")
input("Press Enter to see the next step...")
print("\nStarting to organize files...")
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    if os.path.isdir(file_path):
        continue
    _, file_extension = os.path.splitext(filename)
    moved = False
    for category, extensions in file_types.items():
        if file_extension.lower() in extensions:
            destination_folder = os.path.join(downloads_path, category)
            shutil.move(file_path, destination_folder)
            print(f"✓ Moved {filename} to {category}/")
            moved = True
            break
    
    if not moved:
        print(f"  Left {filename} (unknown type)")

print("\n Organization complete! Check your Downloads folder.")