todos = []
options = {1: "Add todo", 2: "Remove todo", 3: "List todos", 4: "Exit"}


def start():
    def addTodo():
        userTodo = input("Add a todo: ")
        todos.append(userTodo)
        start()

    def removeTodo():
        print("\n".join([todo for todo in todos]))
        rTodo = input("Pick a todo to remove: ")
        todos.remove(rTodo)
        start()

    def listTodo():
        print("\n".join([todo for todo in todos]))
        start()

    def exit():
        print("Goodbye")

    user_text = input(f"What would you like to do? {', '.join(options.values())} ")

    match user_text:
        case "A" | "a":
            addTodo()
        case "R" | "r":
            removeTodo()
        case "L" | "l":
            listTodo()
        case "E" | "e":
            exit()


start()
