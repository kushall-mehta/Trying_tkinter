import tkinter as tk
from tkinter import ttk

def greed():
    pass

root = tk.Tk() #container
root.title("Hello World")

user_name = tk.StringVar()

name_label = tk.Label(root, text="Hello World")
name_label.pack(side="left",padx=(0,10))

name_entry = tk.Entry(root, width=30 , textvariable=user_name)
name_entry.pack(side="left",padx=(0,10))
name_entry.focus()
# root.mainloop
root.mainloop()


