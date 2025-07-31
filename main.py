import os
import random
import time
from datetime import datetime, date


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
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            for id, title, priority, deadline in todos:
                file.write(f"{id}|{title}|{priority}|{statuses[id]}|{deadline}\n")
    except Exception as e:
        print(f"Failed to save file {e}")
    else:
        print("File is saved")


def load():
    todos = []
    statuses = {}
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                id, title, priority, status, deadline = line.strip().split("|")
                todos.append((id, title, priority, deadline))
                statuses[id] = parseBool(status)
        return todos, statuses
    except Exception as e:
        print(f"Failed to load file: {e}")
        return [], {}


def addPryority():
    print("\nSelect priority:")
    print("  1 - 🔴 High")
    print("  2 - 🟡 Medium")
    print("  3 - 🟢 Low")

    priorities = {"1": "high", "2": "medium", "3": "low"}
    choice = input("Input priority(1-3): ").strip()

    priority = priorities.get(choice)

    if priority:
        return priority
    else:
        print("Incorrect choice of priority")
        return None


def inputDeadline():
    date_str = input("Enter deadline (in YYYY-MM-DD format): ")
    try:
        deadline = datetime.strptime(date_str, "%Y-%m-%d").date()
        print("deadline", deadline)
        return deadline
    except ValueError:
        print("Invalid date format. Example: 2025-08-01")
        return None


def addTodo(todos, statuses):
    title = input("Input todo title: ").strip()

    priority = addPryority()

    if not priority:
        return

    deadline = inputDeadline()

    if not deadline:
        return

    id = generateId()

    todos.append((id, title, priority, deadline))
    statuses[id] = False
    save(todos, statuses)


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
        return "[ ]"


def showTodos(statuses):
    def inner(todos):
        for _, (id, title, priority, deadline) in enumerate(todos):
            print(
                f"id: {id}, title: {title}, priority: {priority}, deadline: {deadline}, status: {getStatus(statuses[id])}"
            )

    return inner


def filteredByPriority(todos):
    if len(todos) == 0:
        print("Empty todos")
        return

    priorityOrder = {"high": 0, "low": 2, "medium": 1}
    return sorted(todos, key=lambda todo: priorityOrder.get(todo[2], 99))


def getUpcomingTodos(todos):
    if len(todos) == 0:
        print("Empty todos")
        return

    today = date.today()

    def parse(todo):
        id, title, priority, deadline_str = todo
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        return (id, title, priority, deadline)

    todos_with_dates = [parse(todo) for todo in todos]

    upcoming = [todo for todo in todos_with_dates if todo[3] >= today]
    return sorted(upcoming, key=lambda todo: todo[3])


def changeStatus(todos, statuses, done):
    id = input("Input todo id: ")
    try:
        statuses[id] = done
        save(todos, statuses)
    except IndexError as e:
        print(f"Failed to change status: {e}")


def main():
    while True:
        print("\n--------------------------------------")
        print("Options: ")
        print("  1 - add todo")
        print("  2 - show todos")
        print("  3 - remove todo")
        print("  4 - change status to done")
        print("  5 - change status to not done")
        print("  6 - sorted by upcoming deadline")
        print("  0 - quit")
        print("--------------------------------------\n")

        todos, statuses = load()

        show = showTodos(statuses)

        userInput = input("Input option: ")
        match userInput:
            case "1":
                addTodo(todos, statuses)
            case "2":
                show(filteredByPriority(todos))
            case "3":
                removeTodo(todos, statuses)
            case "4":
                changeStatus(todos, statuses, True)
            case "5":
                changeStatus(todos, statuses, False)
            case "6":
                show(getUpcomingTodos(todos))
            case "0":
                break
            case _:
                print(f"{userInput} - this option does`t exist")


if __name__ == "__main__":
    main()
