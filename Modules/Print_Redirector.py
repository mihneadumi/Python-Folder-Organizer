import tkinter as tk


class PrintRedirector:
    """
    Class to redirect stdout to a ScrolledText widget
    """
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        """Append string to the text widget"""
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END) # Scroll to the end of the console log
