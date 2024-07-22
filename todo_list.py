import tkinter as tk
from tkinter import simpledialog, messagebox
from storage import load_tasks, save_tasks

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = load_tasks()

        self.frame = tk.Frame(root, bg='white')
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, height=10, width=50, bg='white', fg='blue', selectbackground='red')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, bg='white')
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='blue', fg='white')
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='red', fg='white')
        self.delete_button.pack(pady=5)

        self.update_tasks()

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.update_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks()
        else:
            messagebox.showwarning("Delete Task", "No task selected.")

    def update_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
        save_tasks(self.tasks)

    def on_closing(self):
        save_tasks(self.tasks)
        self.root.destroy()
