"""
Run this to start the app
"""
from Modules import PrepareFile, SortFolder
from tkinter.filedialog import askdirectory


path = askdirectory(title='Select Folder to be organised')  # Shows OS dialog box and return the path (poate pusca pe MacOS)
PrepareFile.make_folders(path)
SortFolder.sort_files(path)