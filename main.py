TODOS = []
STATUS = []

def addTodo():
    title = input("Input title: ")
    priority = input("Input priority: ")
    id = 0

    if len(TODOS) > 0:
        id = len(TODOS)

    TODOS.append((id, title, priority))
    STATUS.append(False)
    


def removeTodo():
    indexToRemove = int(input("Input index to remove: "))
    del TODOS[indexToRemove]
    del STATUS[indexToRemove]

def getStatus(status):
    if status:
        return "[✔]"
    else:
       return  "[ ]"    

def showTodos():
    for index ,(id, title, priority) in enumerate(TODOS):
        print(f"id: {id}, title: {title}, priority: {priority}, status: {getStatus(STATUS[index])}")

def changeStatus(done):
    indexToChangeStatus = int(input("Input index of todos which need to change status: "))
    STATUS[indexToChangeStatus]  = done  

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
        userInput = input("Input option: ")
        match userInput:
            case "1":
                addTodo()
            case "2":
                showTodos()
            case "3":
                removeTodo()
            case "4":
                changeStatus(True)
            case "5":
                changeStatus(False)    
            case "0":
                break
            case _:
               print(f"{userInput} - this option does`t exist")             

if __name__ == "__main__":
    main()               