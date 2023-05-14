tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("Select an option:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("> ")

    if choice == "1":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "2":
        show_tasks()
    elif choice == "4":
        print("Exiting...")
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please try again.")
