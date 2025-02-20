from pathlib import Path
import pickle

file = Path("memory.dat")
if file.exists():
    memory = pickle.load(open("memory.dat", "rb"))
else:
    memory = {}


def main_menu():
    mm_choices = input("""
Choose of the following:
1 - Add task
2 - Show tasks
3 - Mark task as completed
4 - Delete task
5 - Save and quit
""")
    if mm_choices == "1":
        add_task()
    elif mm_choices == "2":
        show_tasks()
    elif mm_choices == "3":
        complete_tasks()
    elif  mm_choices == "4":
        delete_tasks()
    elif mm_choices == "5":
        save_exit()
    else:
        print("Invalid input, please try again")
        main_menu()

def add_task():
    task_to_add = input("Enter a task: ")
    memory.update({task_to_add: "❌"})
    print("Task was successfully added")
    input("Press Enter to continue...")
    main_menu()


def show_tasks():
    print(memory)
    input("Press Enter to continue...")
    main_menu()


def complete_tasks():
    n = 1
    list_of_tasks = []
    for task in memory:
        list_of_tasks.append(task)
        print(f" {n} - {list_of_tasks[n-1]}")
        n += 1
    task_to_complete = input("Enter a task to complete: ")
    try:
        memory.update({list_of_tasks[int(task_to_complete)-1] :"✅"})
        print("Task was completed")
        input("Press Enter to continue...")
    except:
            print("Invalid input, please try again")
            complete_tasks()
    main_menu()


def delete_tasks():
    n = 1
    list_of_tasks = []
    n = 1
    for task in memory:
        list_of_tasks.append(task)
        print(f" {n} - {list_of_tasks[n - 1]}")
        n += 1
    task_to_delete = input("Enter a task to delete: ")
    try:
        memory.pop(list_of_tasks[int(task_to_delete)-1])
        print("Task was deleted")
        input("Press Enter to continue...")
    except:
        print("Invalid input, please try again")
    main_menu()


def save_exit():
    pickle.dump(memory, open("memory.dat", "wb"))
    print("ToDoList is saved, have a nice day!")
    exit()


main_menu()