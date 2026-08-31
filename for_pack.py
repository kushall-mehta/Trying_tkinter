import os
import tkinter as tk
from tkinter import filedialog, ttk


root = tk.Tk()
root.title("Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, pady=(4, 0), padx=1)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

text_contents = {}


def get_text_widget():
    selected = notebook.select()
    if not selected:
        return None
    return notebook.nametowidget(selected)


def update_tab_title():
    current = get_text_widget()
    if current is None:
        return

    content = current.get("1.0", "end-1c")
    tab_name = notebook.tab("current", "text")
    current_hash = text_contents.get(str(current))

    if current_hash is None:
        text_contents[str(current)] = hash(content)
        return

    if hash(content) != current_hash:
        if not tab_name.endswith("*"):
            notebook.tab("current", text=tab_name + "*")
    else:
        if tab_name.endswith("*"):
            notebook.tab("current", text=tab_name[:-1])


def create_file(content="", title="Untitled"):
    text_area = tk.Text(notebook, font=("Arial", 11))
    text_area.pack(fill="both", expand=True)
    if content:
        text_area.insert("1.0", content)
    notebook.add(text_area, text=title)
    notebook.select(text_area)

    text_contents[str(text_area)] = hash(content)
    return text_area


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if not file_path:
        return

    selected_tab = notebook.select()
    if not selected_tab:
        return

    text_widget = notebook.nametowidget(selected_tab)
    content = text_widget.get("1.0", "end-1c")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    filename = os.path.basename(file_path)
    notebook.tab(selected_tab, text=filename)
    text_contents[str(text_widget)] = hash(content)


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"Could not open file: {e}")
        return

    filename = os.path.basename(file_path)
    create_file(content, filename)


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=lambda: create_file(), accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")

root.bind("<Control-n>", lambda e: create_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

text_area = create_file()
text_area.bind("<KeyRelease>", lambda event: update_tab_title())

root.mainloop()
