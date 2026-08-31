import tkinter as tk
from tkinter import ttk

def greed():
    print(f"Hello, {user_name.get() or 'World'}")
    pass

root = tk.Tk() #container
root.title("Hello World")

user_name = tk.StringVar()

name_label = tk.Label(root, text="Hello World")
name_label.pack(side="left",padx=(0,10))

name_entry = tk.Entry(root, width=30 , textvariable=user_name)
name_entry.pack(side="left",padx=(0,10))
name_entry.focus()

entery_button = tk.Button(root, text="Enter", command=greed)
entery_button.pack(side="left",fill="x" , expand=True)
# root.mainloop
root.mainloop()




