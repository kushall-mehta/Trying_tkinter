import tkinter as tk
import os
from tkinter import ttk, filedialog

root = tk.Tk()
#
# tk.Label(root, text="Hello World" , bg="red").pack(side="left", fill="y" , expand=True)
# tk.Label(root, text="Hello World", bg="green").pack(side="top" ,fill="x")

def create_file():
    text_area = tk.Text(notebook, font=("Arial", 11))
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="untitled")
    notebook.select(text_area)

def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")
        with open(file_path, "w") as file:
            file.write(content)
    except(AttributeError , FileNotFoundError):
        print("Save operation cancelled")
        return
    notebook.tab("current",text=filename)



root.title("Text Editor")
root.option_add("*tearOff",False)

main  = ttk.Frame(root)
main.pack(fill="both", expand=True , pady = (4,0) , padx = 1)

menu_bar = tk.Menu()
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save", command=save_file)



notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

root.mainloop()
