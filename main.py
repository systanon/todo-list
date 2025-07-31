import os
import random
import time


FILE = "todo.txt"

current_dir = os.path.dirname(__file__)
FILE_PATH = os.path.join(current_dir, FILE)

if not os.path.exists(FILE_PATH):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(" ")
    except:
        print("Failed to create file.")        

def parseBool(s):
    return s.strip().lower() == "true"


def generateId():
    timestamp = int(time.time() * 1000)
    rand_part = random.randint(100, 999)
    return f"{str(timestamp)[-5:]}{rand_part}"    

def save(todos, statuses):
    print("statuses",statuses)
    print("todos",todos)
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            for id, title, priority in todos:
                file.write(f"{id}|{title}|{priority}|{statuses[id]}\n")
    except:
        print(f"Failed to save file")
    else:
        print("File is saved")

def load():
    todos = []
    statuses = {}
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                id, title, priority, status = line.strip().split("|")
                todos.append((id, title, priority))
                statuses[id] = parseBool(status)
            print(statuses)    
        return todos, statuses
    except  Exception as e:
        print(f"Failed to load file: {e}")
        return [], {}
    

def addTodo(todos, statuses):
    title = input("Input todo title: ").strip()

    print("\nSelect priority:")
    print("  1 - 🔴 High")
    print("  2 - 🟡 Medium")
    print("  3 - 🟢 Low")

    priorities = {
        "1": "high",
        "2": "medium",
        "3": "low"
    }
    choice = input("Input priority(1-3): ").strip()

    priority = priorities.get(choice)
    if priority:
        id = generateId()

        todos.append((id, title, priority))
        statuses[id] = False
        save(todos, statuses)
    else:
        print("Incorrect choice of priority")
    


def removeTodo(todos, statuses):
    id = input("Input todo id: ")
    try:
        filteredTodos = [todo for todo in todos if todo[0] != id]
        del statuses[id]
        save(filteredTodos, statuses)
    except IndexError as e:
        print(f"Failed to remove todo: {e}")         

def getStatus(status):
    if status:
        return "[✔]"
    else:
       return  "[ ]"    

def showTodos(todos, statuses):
    if len(todos) > 0:
        for index ,(id, title, priority) in enumerate(todos):
            print(f"id: {id}, title: {title}, priority: {priority}, status: {getStatus(statuses[id])}")
    else:
        print("Empty todos")

def changeStatus(todos, statuses, done):
    id = input("Input todo id: ")
    try:
        statuses[id] = done
        save(todos, statuses)
    except IndexError as e:
        print(f"Failed to change status: {e}")      

def main():
    while True:
        print("--------------------------------------")
        print("Options: ")
        print("1 - add todo: ")
        print("2 - show todos: ")
        print("3 - remove todo: ")
        print("4 - change status to done: ")
        print("5 - change status to not done: ")
        print("--------------------------------------")

        todos, statuses = load()

        userInput = input("Input option: ")
        match userInput:
            case "1":
                addTodo(todos, statuses)
            case "2":
                showTodos(todos, statuses)
            case "3":
                removeTodo(todos, statuses)
            case "4":
                changeStatus(todos, statuses, True)
            case "5":
                changeStatus(todos, statuses, False)    
            case "0":
                break
            case _:
               print(f"{userInput} - this option does`t exist")             

if __name__ == "__main__":
    main()               