import tkinter as tk
from tkinter import messagebox
import json


# initialize the task list
tasks =[]
# function to add task
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append({"id": len(tasks)+1, "title": task, "completed": False})
        update_tasks_list()
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","Task cannot be empty")

# function to mark task as completed
def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_tasks_list()
    else:
        messagebox.showwarning("warning","No task selected")
def update_tasks_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_text = task["title"]
        if task["completed"]:
            task_text += " (Completed)"
        task_listbox.insert(tk.END, task_text)

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index =selected[0]
        del tasks[index]
        update_tasks_list()
    else:
        messagebox.showwarning("warning","No task selected")
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    messagebox.showinfo("success","Tasks saved successfully")
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        update_tasks_list()
    except FileNotFoundError:
        messagebox.showwarning("warning","No saved tasks found")
        
# Define dark theme colors
dark_theme_colors ={
    "bg": "#2e2e2e",   # Background color
    "fg": "#ffffff",   # Foreground (text) color
    "entry_bg": "#3e3e3e",
    "button_bg": "#444444",
    "button_fg": "#ffffff",
    "listbox_bg": "#3e3e3e",
    "listbox_fg": "#ffffff"
}

# ==================Create Main Window======================
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
root.configure(bg=dark_theme_colors["bg"])
# task entry
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task, bg=dark_theme_colors["button_bg"], fg=dark_theme_colors["button_fg"])
add_task_button.pack(pady=10)

# mark button as completed
mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack(pady=5)

# delete button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Save button
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=5)

# Load button
load_button =  tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack(pady=5)

# task listbox
task_listbox = tk.Listbox(root, width=50, height=15, bg=dark_theme_colors['listbox_bg'])
task_listbox.pack(pady=10)
root.mainloop()