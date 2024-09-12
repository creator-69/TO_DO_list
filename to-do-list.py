def show_menu():
    print("\nTo-Do List Manager")
    print(" Add Task")
    print(" Show Tasks")
    print(" Delete Task")
    print(" Exit")

def add_task(task_list):
    task = input("Enter the new task: ")
    task_list.append(task)
    print("Task added successfully!")

def show_tasks(task_list):
    if not task_list:
        print("The task list is empty.")
    else:
        print("\nTask List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def delete_task(task_list):
    show_tasks(task_list)
    try:
        number = int(input("eEnter tthe task number to delete: "))
        if 1 <= number <= len(task_list):
            removed_task = task_list.pop(number - 1)
            print(f"Task '{removed_task}' deleted successfully")
        else:
            print("Invasdas number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        show_menu()
        choice = input("Enter your choice : ")
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            show_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again")

main()
