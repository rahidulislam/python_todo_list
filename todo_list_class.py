import json


class TodoList:
    def __init__(self):
        """Initialize the TodoList class."""
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        """Add a new task to the list"""
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        """Display all tasks in the list"""
        if not self.tasks:
            print("No tasks available")
            return
        print("\nYour tasks:")
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']}. {task['title']} [{status}]")

    def edit_task(self, task_id, new_title):
        """Edit the title of a task"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                print(f"Task ID {task_id} updated")
                return
        print(f"Task ID {task_id} not found")

    def mark_task_completed(self, task_id):
        """mark a task as completed by its ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task ID {task_id} marked as completed")
                return
        print(f"Task ID {task_id} not found")

    def delete_task(self, task_id):
        """Delete a task by its ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} is deleted")
                return
        print(f"Task ID {task_id} not found")

    def save_tasks_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
        print("Tasks saved successfully.")

    def load_tasks_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
            if self.tasks:
                self.next_id = max(task["id"] for task in self.tasks) + 1

                print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")


# main program
def main():
    todo = TodoList()
    todo.load_tasks_from_file()
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Edit a task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Save tasks to file")
        print("7. Load tasks from file")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to edit: "))
                new_title = input("Enter new title: ")
                todo.edit_task(task_id, new_title)
            except ValueError:
                print("Invalid task ID. Please try again.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_task_completed(task_id)
            except ValueError:
                print("Invalid task ID. Please try again.")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please try again.")
        elif choice == "6":
            todo.save_tasks_to_file()
        elif choice == "7":
            todo.load_tasks_from_file()
        elif choice == "8":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# call the main function
if __name__ == "__main__":
    main()
