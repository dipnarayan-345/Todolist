import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

def edit_task():
    try:
        selected_task_index = task_list.curselection()[0]
        selected_task = task_list.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, selected_task)
        task_list.delete(selected_task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("TO-DO List Application")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Task List
task_list = tk.Listbox(root, width=40, selectmode=tk.SINGLE)
task_list.pack()

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
edit_button = tk.Button(root, text="Edit Task", command=edit_task)

add_button.pack(pady=5)
delete_button.pack(pady=5)
edit_button.pack(pady=5)

# Start the GUI application
root.mainloop()