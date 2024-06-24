class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added.")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            print("Task updated.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task index.")

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            print("Task status toggled.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Toggle Task Status")
        print("5. List Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task index: "))
            description = input("Enter new description: ")
            todo_list.update_task(index, description)
        elif choice == '3':
            index = int(input("Enter task index: "))
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Enter task index: "))
            todo_list.toggle_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
