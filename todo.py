import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added.")

    def delete_task(self):
        self.show_tasks()
        task_no = int(input("Enter the task number to delete: "))
        if 0 < task_no <= len(self.tasks):
            del self.tasks[task_no - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def main_menu(self):
        while True:
            print("\nTo-Do List App")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoList()
    app.main_menu()
