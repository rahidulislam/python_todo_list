# To-Do List Application

Here’s a step-by-step guide to creating a **To-Do List Application** in Python. The application will be simple and console-based, allowing users to manage tasks effectively.

---

### **Step 1: Define the Requirements**

Before coding, list the features you want:

1. Add a task.
2. View all tasks.
3. Mark a task as complete.
4. Delete a task.
5. Save tasks to a file and load them back.

---

### **Step 2: Plan the Application Structure**

- Use a list to store tasks.
- Each task can be a dictionary with properties like:
  - `id`: A unique identifier.
  - `title`: The task description.
  - `completed`: A boolean indicating if the task is done.

---

### **Step 3: Write the Code**

#### **1. Initialize the Project**

Start with a basic structure:

```python
# to_do_list.py

# Initialize the task list
tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")
```

---

#### **2. Add a Task**

Create a function to add tasks:

```python
def add_task():
    title = input("Enter the task: ")
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    print(f"Task '{title}' added.")
```

---

#### **3. View All Tasks**

Create a function to display tasks:

```python
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour Tasks:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. {task['title']} [{status}]")
```

---

#### **4. Mark a Task as Completed**

Create a function to update task status:

```python
def mark_task_completed():
    task_id = int(input("Enter the task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task '{task['title']}' marked as completed.")
            return
    print("Task not found.")
```

---

#### **5. Delete a Task**

Create a function to delete tasks:

```python
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Task ID {task_id} deleted.")
```

---

#### **6. Save and Load Tasks**

Use `json` to save and load tasks:

```python
import json

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved to tasks.json.")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")
```

---

#### **7. Create the Main Program Loop**

Bring everything together:

```python
while True:
    display_menu()
    choice = input("Choose an option: ")
    
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
```

---

### **Step 4: Test the Application**

1. Run the program.
2. Test each feature:
   - Add a few tasks.
   - View tasks to check the list.
   - Mark a task as complete.
   - Delete a task.
   - Save tasks to a file and reload them.

---

### **Step 5: Enhance the Application**

After implementing the basic version, you can add these features:

1. **Priority Levels**: Allow users to assign priorities (e.g., High, Medium, Low).
2. **Due Dates**: Add a due date for tasks and display overdue tasks.
3. **Sorting**: Enable sorting by completion status, due date, or priority.
4. **GUI**: Use a library like `tkinter` to build a graphical user interface.

---

This structured approach ensures you understand the logic and learn core Python skills effectively. Let me know if you'd like enhancements or code explanations!