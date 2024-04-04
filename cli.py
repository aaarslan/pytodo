class TodoCliApp:
    def __init__(self):
        self.todos = []
        self.options = {1: "Add todo", 2: "Remove todo", 3: "List todos", 4: "Quit"}
        self.actions = {
            "a": self.add_todo,
            "r": self.remove_todo,
            "l": self.list_todos,
            "q": self.quit,
        }

    def add_todo(self):
        """Add a todo to the list."""
        user_todo = input("Add a todo: ")
        self.todos.append(user_todo)
        return True

    def remove_todo(self):
        """Remove a todo from the list."""
        print("\n".join([todo for todo in self.todos]))
        r_todo = input("Pick a todo to remove: ")
        self.todos.remove(r_todo)
        return True

    def list_todos(self):
        """List all todos."""
        print("\n".join([todo for todo in self.todos]))
        return True

    def quit(self):
        """Quit the application."""
        print("Goodbye")
        return False

    def start(self):
        """Start the application."""
        while True:
            user_text = input(
                f"What would you like to do? {', '.join(self.options.values())} "
            ).lower()
            action = self.actions.get(user_text)
            if action and not action():
                break


app = TodoCliApp()
app.start()
