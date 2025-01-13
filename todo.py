# Todo list application
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Tâche ajoutée : {task}")

def show_tasks():
    if not todo_list:
        print("Aucune tâche pour le moment.")
    else:
        print("Liste des tâches :")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")


add_task("Finir le projet")
show_tasks()

