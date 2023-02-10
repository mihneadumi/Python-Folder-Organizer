from tkinter.filedialog import askdirectory
import tkinter as tk
import PrepareFile
import SortFolder

class UI:

    def __init__(self):
        self.path = None
    
    def print_main(self):
        print('-------Main Menu-------\n')
        self.print_selected_folder()
        print('\n1. Select folder')
        print('2. Sort files')
        print('3. Sort files and delete empty folders')
        print('0. Exit')
        print('-----------------------')
    
    def print_selected_folder(self):
        print(f'Current folder: {self.path}')

    def get_input(self):
        return input('Select an option: ')
    
    def get_path(self):
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        self.path = askdirectory(parent=root, initialdir="/", title='Please select a directory')
        root.destroy()

    def start_app(self):
        while True:
            self.print_main()
            option = self.get_input()
            if option == '1':
                self.get_path()
            elif option == '2':
                if self.path:
                    PrepareFile.make_folders(self.path)
                    SortFolder.sort_files(self.path)
                else:
                    print('No folder selected!')
            elif option == '3':
                if self.path:
                    PrepareFile.make_folders(self.path)
                    SortFolder.sort_files(self.path)
                    PrepareFile.delete_empty_folders(self.path)
                else:
                    print('No folder selected!')
            elif option == '0':
                exit()
            else:
                print('Invalid option!')
