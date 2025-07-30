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

def save(todos, statuses):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            for (id, title, priority), status in zip(todos, statuses):
                file.write(f"{id}|{title}|{priority}|{status}\n")
    except:
        print("Failed to save file.")
    else:
        print("File is saved")

def load():
    todos = []
    statuses = []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                id, title, priority, status = line.strip().split("|")
                todos.append(((int(id)), title, priority))
                statuses.append(parseBool(status))
        return todos, statuses
    except  Exception as e:
        print(f"Failed to load file: {e}")
        return [], []
    

def addTodo(todos, statuses):
    title = input("Input title: ")
    priority = input("Input priority: ")
    id = 0

    if len(todos) > 0:
        id = len(todos)

    todos.append((id, title, priority))
    statuses.append(False)
    save(todos, statuses)
    


def removeTodo(todos, statuses):
    indexToRemove = int(input("Input index to remove: "))
    try:
        del todos[indexToRemove]
        del statuses[indexToRemove]
        save(todos, statuses)
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
            print(f"id: {id}, title: {title}, priority: {priority}, status: {getStatus(statuses[index])}")
    else:
        print("Empty todos")

def changeStatus(todos, statuses, done):
    indexToChangeStatus = int(input("Input index of todos which need to change status: "))
    try:
        statuses[indexToChangeStatus]  = done
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