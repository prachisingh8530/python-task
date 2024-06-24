import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        self.button_add = tk.Button(root, text="Add Task", command=self.add_task)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_update = tk.Button(root, text="Update Task", command=self.update_task)
        self.button_update.pack(side=tk.LEFT, padx=10)

        self.button_delete = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.button_delete.pack(side=tk.LEFT, padx=10)

        self.button_toggle = tk.Button(root, text="Toggle Task", command=self.toggle_task)
        self.button_toggle.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        description = self.entry_task.get()
        if description:
            task = Task(description)
            self.tasks.append(task)
            self.update_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            description = self.entry_task.get()
            if description:
                self.tasks[index].description = description
                self.update_listbox()
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task description cannot be empty.")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def toggle_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index].completed = not self.tasks[index].completed
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task.description}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
