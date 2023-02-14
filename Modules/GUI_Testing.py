import tkinter as tk
import tkinter.scrolledtext as tkst

root = tk.Tk()
root.title("GUI")
root.geometry("450x250")
root.resizable(False, False)
root.configure(bg="white", padx=10, pady=10, relief="groove", borderwidth=5, cursor="arrow", takefocus=True)


# Create a label with unmodifiable text on the same line as button 1
label = tk.Label(root, text="This text is on the same line as Button 1")
label.grid(row=0, column=0)

# Create Button 1 and add it to the window
button1 = tk.Button(root, text="Button 1")
button1.grid(row=0, column=1, padx=10)

# Create a frame to hold the other two buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=2)

# Create Button 2 and add it to the frame
button2 = tk.Button(button_frame, text="Button 2")
button2.grid(row=0, column=0, padx=10)

# Create Button 3 and add it to the frame
button3 = tk.Button(button_frame, text="Button 3")
button3.grid(row=0, column=1, padx=10)

# Create a scrolled text widget to display the console log at the bottom

console = tkst.ScrolledText(root, height=10, width=50, wrap=tk.WORD, state="disabled")
console.grid(row=2, column=0, columnspan=2)


# Function to print a message to the console log
def log(message):
    console.config(state="normal")
    console.insert(tk.END, message + "\n")
    console.see(tk.END)
    console.config(state="disabled")

# Bind the buttons to event handler functions that print messages to the console log
button1.config(command=lambda: log("Button 1 clicked"))
button2.config(command=lambda: log("Button 2 clicked"))
button3.config(command=lambda: log("Button 3 clicked"))

root.mainloop()
