import os
# from tkinter import Tk
import sys
from tkinter.filedialog import askdirectory


class File:  # Makes my life easier and the code cleaner
    def __init__(self, path: str, root=''):
        tupp = os.path.splitext(path)
        self.path = root + '/' + path
        self.filename = tupp[0]
        self.ext = tupp[1]


def create_folder(name: str, path: str):
    folder_path = path + "/" + name
    os.mkdir(folder_path)


def make_folders():
    path = askdirectory(title='Select Folder to be organised')  # Shows OS dialog box and return the path (poate pusca pe MacOS)
    if path == '':
        print("No folder selected...\nExiting...")
        sys.exit()
    folder_dict = check_folders(path)
    for folder in folder_dict.keys():
        if folder_dict[folder] == False:
            print(f"Missing {folder} folder!")
            create_folder(folder, path)
            print(f"Created {folder} folder.")

    print("\033[92mAll required folders are present!") # Used ANSI Escape sequence to make text green


def check_folders(path):
    folder_dict = {'Documents': False, 'Pictures': False, 'Videos': False, 'Zips': False, 'Apps': False}
    for dirname in os.listdir(path):
        selected_file = File(dirname, path)
        if selected_file.ext == '':  # Folders have no extension
            if selected_file.filename in folder_dict.keys():
                folder_dict[selected_file.filename] = True

    return folder_dict
