import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="#f0f0f0")

tasks = []

# Functions
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        task = listbox_tasks.get(index)
        confirm = messagebox.askyesno("Delete Task", f"Delete '{task}'?")
        if confirm:
            tasks.pop(index)
            update_listbox()
    else:
        messagebox.showinfo("Info", "Select a task to delete.")

def mark_done():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        tasks[index] = f"✔️ {task}"
        update_listbox()

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

# Widgets
label_title = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", command=add_task, width=10)
btn_add.pack(pady=5)

btn_done = tk.Button(root, text="Mark as Done", command=mark_done, width=10)
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task, width=10)
btn_delete.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=45, height=10)
listbox_tasks.pack(pady=10)

# Run the app
root.mainloop()