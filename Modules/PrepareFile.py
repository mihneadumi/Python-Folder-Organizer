import os
import sys


class File:  # Makes my life easier and the code cleaner
    def __init__(self, path: str, root=''):
        tupp = os.path.splitext(path)
        self.root = root
        self.path = root + '/' + path
        self.filename = tupp[0]
        self.extension = tupp[1]


def create_folder(name: str, path: str):
    folder_path = path + "/" + name
    os.mkdir(folder_path)


def make_folders(path: str):
    if path == '':
        print("No folder selected...\nExiting...")
        sys.exit()
    folder_dict = check_folders(path)
    for folder in folder_dict.keys():
        if folder_dict[folder] == False:  # Creates required folder if it doesn't already exist
            print(f"Missing {folder} folder!")
            create_folder(folder, path)
            print(f"Created {folder} folder.")

    print("\033[92mAll required folders are present!\033[0m")  # Used ANSI Escape sequence to make text green


def check_folders(path):
    """
    Gets a "dictionary of existance" for each folder (True = it already exists, False otherwise)
    :param path: the path that will be verified for required folders
    :return: a dictionary with boolean values for each required folder
    """
    folder_dict = {'Documents': False, 'Pictures': False, 'Videos': False, 'Zips': False, 'Apps': False,'Music': False, 'Other':False}
    for dirname in os.listdir(path):
        selected_file = File(dirname, path)
        if selected_file.extension == '':  # Folders have no extension
            if selected_file.filename in folder_dict.keys():
                folder_dict[selected_file.filename] = True

    return folder_dict

def delete_empty_folders(path: str):
    for dirname in os.listdir(path):
        selected_file = File(dirname, path)
        if selected_file.extension == '':  # Folders have no extension
            if len(os.listdir(selected_file.path)) == 0: # Checks if folder is empty
                os.rmdir(selected_file.path)
                print(f"Deleted {selected_file.filename} folder.")

    print("\033[92mAll empty folders deleted!\033[0m")
