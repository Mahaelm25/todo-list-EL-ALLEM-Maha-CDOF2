# Todo list application
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"\nTask added successfully: {task}")

def show_tasks():
    if not todo_list:
        print("\nYour to-do list is currently empty. Add a task to get started!")
    else:
        print("\nHere are your current tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed = todo_list.pop(task_number - 1)
        print(f"\nTask removed: {removed}")
    else:
        print("\nInvalid task number. Please enter a valid number.")

def display_menu():
    print("\n=== To-Do List Manager ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

while True:
    display_menu()
    choice = input("\nWhat would you like to do? (1-4): ")

    if choice == "1":
        task = input("\nEnter the task description: ")
        if task.strip():
            add_task(task)
        else:
            print("\nPlease enter a valid task.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        if todo_list:
            try:
                task_num = int(input("\nEnter the task number to remove: "))
                delete_task(task_num)
            except ValueError:
                print("\nPlease enter a valid number.")
        else:
            print("\nYour to-do list is empty, nothing to remove.")

    elif choice == "4":
        print("\nThank you for using the to-do list manager. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please select an option between 1 and 4.")
