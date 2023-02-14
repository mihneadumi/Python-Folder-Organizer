import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Folder Organizer")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.root.configure(bg="white", padx=10, pady=10, relief="flat", borderwidth=5, cursor="arrow", takefocus=True)

    # Create UI elements
    def add_elems(self):
        folder_label = tk.Label(self.root, text="Selected folder: ")
        folder_label.configure(font=("Arial", 8), bg="white", fg="black", relief="flat", borderwidth=1, cursor="arrow")
        folder_label.grid(row=0, column=0, sticky="nsew")

        folder_path = tk.Entry(self.root, width=50, font=("Arial", 12))
        folder_path.configure(background="white", relief="solid", borderwidth=1, cursor="arrow")
        folder_path.grid(row=0, column=1, padx=10, sticky="nsew")

        select_folder_button = tk.Button(self.root, text="...", font=("Arial", 8))
        select_folder_button.configure(background="white", relief="solid", borderwidth=0.5, cursor="arrow")
        select_folder_button.grid(row=0, column=2)

        sort_button = tk.Button(self.root, text="Sort files", font=("Arial", 12))
        sort_button.configure(background="white", relief="solid", borderwidth=1, cursor="arrow")
        sort_button.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

        sort_and_delete_button = tk.Button(self.root, text="Sort files and delete empty folders", font=("Arial", 12))
        sort_and_delete_button.configure(background="white", relief="solid", borderwidth=1, cursor="arrow")
        sort_and_delete_button.grid(row=2, column=0, columnspan=3, ipady=10, sticky="nsew")


        self.root.mainloop()

