import tkinter as tk
from tkinter import ttk

def greed():
    print("hello")
# def quit():
# greed()

root = tk.Tk() #container
root.title("Hello World")

# root.mainloop
greed_button = ttk.Button(root, text="Greed", command=greed)#button
greed_button.pack(side="left" ,fill="x" , expand=True) #it will dispay on screen

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left" ,fill="x" , expand=True)

root.mainloop()
