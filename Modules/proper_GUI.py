import sys
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText

import colorama

from Modules import PrepareFile, SortFolder, Print_Redirector

def GUI():
    root = tk.Tk()
    root.title("Folder Organizer")
    root.geometry("505x350")
    root.resizable(False, False)
    root.configure(bg="white", padx=10, pady=10, relief="flat", borderwidth=5, cursor="arrow", takefocus=True)

    path = tk.StringVar()
    path.set(" No folder selected")

    # Create UI elements
    folder_label = tk.Label(root, text="Selected folder: ")
    folder_label.configure(font=("Arial", 8), bg="white", fg="black", relief="flat", borderwidth=1, cursor="arrow")
    folder_label.grid(row=0, column=0, sticky="nsew")

    folder_path = tk.Entry(root, width=50, font=("Arial", 10), textvariable=path, state="disabled")
    folder_path.configure(background="white", relief="solid", borderwidth=1, cursor="arrow")
    folder_path.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

    select_folder_button = tk.Button(root, text="...", font=("Arial", 8))
    select_folder_button.configure(background="white", relief="solid", borderwidth=0.5, cursor="arrow", command=lambda: select_path(path))
    select_folder_button.grid(row=0, column=2, ipadx=1, pady=5, sticky="nsew")

    spacer = tk.Label(root, text="")
    spacer.configure(font=("Arial", 8), bg="white", fg="black", relief="flat", borderwidth=1, cursor="arrow")
    spacer.grid(row=1, column=0, columnspan=3)

    sort_button = tk.Button(root, text="Sort files", font=("Arial", 12))
    sort_button.configure(background="white", relief="solid", borderwidth=1, cursor="arrow", command=lambda: sort_files(path))
    sort_button.grid(row=2, column=0, columnspan=3, pady=5, ipady=10, sticky="nsew")

    sort_and_delete_button = tk.Button(root, text="Sort files and delete empty subfolders", font=("Arial", 12))
    sort_and_delete_button.configure(background="white", relief="solid", borderwidth=1, cursor="arrow", command=lambda: sort_and_delete(path))
    sort_and_delete_button.grid(row=3, column=0, columnspan=3, pady=5, ipady=10, sticky="nsew")

    console = ScrolledText(root, height=10, width=50, wrap=tk.WORD)
    console.configure(background="white", relief="solid", borderwidth=1, cursor="arrow", font=("Arial", 8))
    console.grid(row=4, column=0, columnspan=3, pady=5, sticky="nsew")

    colorama.init()
    sys.stdout = Print_Redirector.PrintRedirector(console)
    # sys.stderr = Print_Redirector.PrintRedirector(console)

    root.mainloop()

def start_app():
    GUI()


if __name__ == '__main__':
    start_app()


def select_path(path):
    path_str = askdirectory()
    path.set(path_str)

def sort_files(path):
    if path.get() != " No folder selected" and path.get() != "":
        PrepareFile.make_folders(path.get())
        SortFolder.sort_files(path.get())
    else:
        print("\033[93mNo folder selected\033[0m")
def sort_and_delete(path):
    if path.get() != " No folder selected" and path.get() != "":
        PrepareFile.make_folders(path.get())
        SortFolder.sort_files(path.get())
        PrepareFile.delete_empty_folders(path.get())
    else:
        print("\033[93mNo folder selected\033[0m")

