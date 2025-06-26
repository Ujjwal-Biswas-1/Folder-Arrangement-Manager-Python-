import os
import shutil

folder_path = ""  # opening folder



def get_categories(files):  # getting its extension
        extension = os.path.splitext(files)[1].lower()

        file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt", ".pptx"],
            "Videos": [".mp4", ".mkv", ".avi"],
            "Music": [".mp3", ".wav"],
            "Archives": [".zip", ".rar", ".7z"],
        }
        for catagory, extensions in file_types.items():
            if extension in extensions:
                return catagory
        return "others"  # diving it on basis of extension




def organise_main(folder_path):
    all_files = os.listdir(folder_path)  # getting fiels

    for files in all_files:  # looping throgh every file
        # real full path of exact file(not only from folder basis)
        full_file_path = os.path.join(folder_path, files)

        if os.path.isfile(full_file_path):  # cheaking if it returns real catagories
            catagory_check = get_categories(files)
            # now we have folder names for catagories
            catagory_path = os.path.join(folder_path, catagory_check)

            # here we created the directory for catagories
            os.makedirs(catagory_path, exist_ok=True)

            # puts files in there catagory folder
            final_destination = os.path.join(catagory_path, files)

            if (os.path.exists(final_destination)):  # if name already exist
                base, ext = os.path.splitext(files)
                i = 1
                new_updated_file_name = f"{base}{i}{ext}"  # add number after it
                new_final_destination = os.path.join(
                    catagory_path, new_updated_file_name)

                while (os.path.exists(new_final_destination)):  # add number after every such file
                    i += 1
                    new_updated_file_name = f"{base}{i}{ext}"
                    new_final_destination = os.path.join(
                        catagory_path, new_updated_file_name)

                final_destination = new_final_destination

            shutil.move(full_file_path, final_destination)  # this moves the files

            print(f"moved {files}  to ---{catagory_check}")

    print(f"process completed ..\n")
