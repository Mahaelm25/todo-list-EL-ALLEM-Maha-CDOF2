# Simple To-Do List Application

tasks = []  # List to store tasks as dictionaries

def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter the task description: ").strip()
    if not task:
        print("Error: Task description cannot be empty. Try again.")
        return
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def list_tasks():
    """List all tasks with their completion status."""
    if not tasks:
        print("\nNo tasks available!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "DONE" if task["completed"] else "PENDING"
        print(f"{index}. {task['task']} [{status}]")

def mark_complete():
    """Mark a task as completed."""
    if not tasks:
        print("\nNo tasks available to mark as completed!")
        return
    try:
        list_tasks()
        index = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print(f"Task '{tasks[index - 1]['task']}' marked as DONE!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task():
    """Delete a task by its number."""
    if not tasks:
        print("\nNo tasks available to delete!")
        return
    try:
        list_tasks()
        index = int(input("\nEnter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    """Main loop to interact with the user."""
    print("Welcome to your personal To-Do List!")
    while True:
        print("\nMenu:")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark Task as DONE")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Thanks for using the To-Do List.")
            break
        else:
            print("Error: Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()

