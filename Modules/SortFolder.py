import os
import shutil
from Modules.PrepareFile import File


def get_folder(extension: str):
    """
    Returns a string with the destination folder name to be concatenated at the end of working directory path
    """
    doc_extensions = ['.txt', '.docx', '.doc', '.pdf', '.xlsx', '.xls', '.pptx', '.ppt']
    pic_extensions = ['.jpg', '.jpeg', '.png', '.svg', '.webp', '.ico', '.bmp', '.tif', '.tiff']
    vid_extensions = ['.mp4', '.mov', '.gif', '.wmv', '.avi', '.avchd', '.mpeg-2']
    app_extensions = ['.exe']
    zip_extensions = ['.zip', '.rar', '.7z']
    mus_extensions = ['.mp3', '.aac', '.wav', '.aiff', '.m4a', '.flac']

    if extension in doc_extensions:
        return '/Documents'
    elif extension in pic_extensions:
        return '/Pictures'
    elif extension in vid_extensions:
        return '/Videos'
    elif extension in app_extensions:
        return '/Apps'
    elif extension in zip_extensions:
        return '/Zips'
    else:
        return '/Other'

def sort_files(root: str):
    print('\033[93mMoving files...\033[0m')
    for file_str in os.listdir(root):
        file = File(file_str, root)
        if file.extension: # Skips folders bcs they have no extension
            try:
                dest = file.root + get_folder(file.extension)
                shutil.move(file.path, dest)
            except TypeError as te:

                print (f'{file.filename} could not be moved!')

    print("\033[92mDirectory succesfully organized!\033[0m")
