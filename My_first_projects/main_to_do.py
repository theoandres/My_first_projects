store = []

def choice_1():
    global store
    new_task = input("New task:")
    store.append(new_task)
    print("New task was successfully added! :)")
    action()


def choice_2():
    print(store)
    action()


def choice_3():
    print("Choose task to complete ↓")
    n = 0
    for task in store:
        print(f" {n+1} - {task}")
        n+=1
    complete_choice = int(input())
    if 0 <= complete_choice < len(store):
        store[complete_choice - 1] = store[complete_choice - 1] + " ✓"
        print(f"Congrats, your task was successfully completed!")
    else:
        print("Invalid value, please try again")
    action()


def choice_4():
    print("Choose task to delete ↓")
    n = 0
    for task in store:
        print(f" {n+1} - {task}")
        n += 1
    delete_choice = int(input())
    if 0 <= delete_choice < len(store):
        store.pop(delete_choice - 1)
        print(f"Your task was deleted!")
        action()
    else:
        print("Invalid value, please try again")


def choice_5():
    exit()

def action():
    while True:
        action = input("""
        1 - Main menu
        2 - Exit
        """)
        if action == "1":
            main_menu()
            break
        elif action == "2":
            choice_5()
        else:
            print("Invalid input, please try again")


def main_menu():
    choice = input("""
    1 - Add task
    2 - Show tasks
    3 - Mark task as completed
    4 - Delete task
    5 - Save and quit
    """)
    if choice == "1":
        choice_1()
    elif choice == "2":
        choice_2()
    elif choice == "3":
        choice_3()
    elif choice == "4":
        choice_4()
    elif choice == "5":
        choice_5()
    else:
        print("Invalid input, please try again")
        main_menu()


main_menu()
