import json
# initialize the task list
task_list = []

# function to display the main menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

# function to add a task to the list
def add_task():
    title = input("Enter task title: ")
    task_id = len(task_list)+1
    task_list.append({"id": task_id, "title": title, "completed": False})
    print(f"Task '{title}' added successfully.")

# function to view all tasks in the list
def view_tasks():
    if not task_list:
        print("No Tasks Available.")
        return
    print("\nYour Tasks:")
    for task in task_list:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. {task["title"]} [{status}]")

# function to mark a task as completed
def mark_task_completed():
    task_id = int(input("Enter the task ID to mark as completed: "))
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task '{task['title']}' marked as completed.")
            return
    print("Task not found.")

# function to remove a task from the list
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    global task_list
    task_list = [task for task in task_list if task["id"] != task_id]
    print(f"Task with ID {task_id} deleted.")
    
# function to save the task list to a file
def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(task_list, file)
    print("Tasks saved successfully.")

# function to load the task list from a file
def load_tasks():
    global task_list
    try:
        with open("tasks.json","r") as file:
            task_list = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")

# main program loop
while True:
    display_menu()
    choice = input("Choose an option:")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        load_tasks()
    elif choice == "7":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
