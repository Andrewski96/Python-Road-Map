import os
import json

TODO_FILE = "todo_list.json"

def showTask(value):
    if not value:
        print('No tasks yet!')
    else:
        for i, task in enumerate(value):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i + 1}. {status} {task['Task']}")
def addTask(value):
    newTask = input('Enter task: ')
    value.append({"Task": newTask, "done": False})
    print(f"\'{newTask}\' Added!")
def markTask(value):
    showTask(value)
    try:
        valueMark = int(input('Task number to mark done: ')) - 1
        value[valueMark]["done"] = True
        print(f"Task marked done")
    except (ValueError, IndexError):
        print('Invalid input.')

def unmarkTask(value):
    showTask(value)
    try:
        valueMark = int(input('Task number to mark done: ')) - 1
        value[valueMark]["done"] = False
        print(f"Task unmarked done")
    except (ValueError, IndexError):
        print('Invalid input.')
def delTask(value):
    showTask(value)
    try:
        delIndex = int(input('Enter what task to delete: ')) - 1
        remove = value.pop(delIndex)
        print(f'Deleted {remove}')
    except(ValueError,IndexError):
        print('Invalid option.')
def saveTask(value):
    with open(TODO_FILE, "w") as f:
        json.dump(value, f, indent=2)
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []
def main():
    tasks = load_tasks()
    while True:
        print("To Do List")
        print("V) View Tasks")
        print("A) Add Tasks")
        print("B) Mark Tasks as done")
        print("C) Unmark Tasks as done")
        print("D) Delete Tasks")
        print("E) Exit")
        choice = input('Choose an option: ')
        toUpperChoice = choice.upper()
        if toUpperChoice == 'V':
            showTask(tasks)
        elif toUpperChoice == 'A':
            addTask(tasks)
        elif toUpperChoice == 'B':
            markTask(tasks)
        elif toUpperChoice == 'C':
            unmarkTask(tasks)
        elif toUpperChoice == 'D':
            delTask(tasks)
        elif toUpperChoice == 'E':
            saveTask(tasks)
            print("Thank you for using our services!")
            break
        else:
            print('You have entered in an invalid response.')

if __name__ == "__main__":
    main()