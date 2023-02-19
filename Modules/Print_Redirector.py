import tkinter as tk


class PrintRedirector:
    """
    Class to redirect stdout to a ScrolledText widget
    """
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, cmd):
        if cmd.startswith("\033"):
            cmd = cmd[5:-4]

        self.text_widget.insert(tk.END, cmd)
        self.text_widget.see(tk.END) # Scroll to the end of the console log
