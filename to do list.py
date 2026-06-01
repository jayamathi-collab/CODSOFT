import tkinter as tk
from tkinter import messagebox

def update_count():
    count = task_listbox.size()
    count_label.config(text=f"Total Tasks: {count}")

def add_task():
    task = task_entry.get().strip()

    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_count()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to update!")
        return

    new_task = task_entry.get().strip()

    if not new_task:
        messagebox.showwarning("Warning", "Enter updated task!")
        return

    task_listbox.delete(selected[0])
    task_listbox.insert(selected[0], new_task)
    task_entry.delete(0, tk.END)
    update_count()

def delete_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete!")
        return

    task_listbox.delete(selected[0])
    update_count()

def select_task(event):
    selected = task_listbox.curselection()

    if selected:
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_listbox.get(selected[0]))

# Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")

title = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_task).grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
task_listbox.pack(pady=15)
task_listbox.bind("<<ListboxSelect>>", select_task)

# Tracking label
count_label = tk.Label(root, text="Total Tasks: 0", font=("Arial", 12))
count_label.pack(pady=5)

root.mainloop()