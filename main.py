import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.todos = []
        self.setup_ui()

    def setup_ui(self):
        """Set up the GUI components."""
        self.root.title("Todo Application")

        # Input field for new todo
        self.todo_entry = tk.Entry(self.root, width=50)
        self.todo_entry.pack()

        # Add todo button
        self.add_button = tk.Button(self.root, text="Add Todo", command=self.add_todo)
        self.add_button.pack()

        # Listbox to display todos
        self.todo_listbox = tk.Listbox(self.root, width=50, height=15)
        self.todo_listbox.pack()

        # Remove todo button
        self.remove_button = tk.Button(
            self.root, text="Remove Selected Todo", command=self.remove_todo
        )
        self.remove_button.pack()

    def add_todo(self):
        """Add a todo to the list and refresh the listbox."""
        todo = self.todo_entry.get()
        if todo:  # Ensure the todo is not empty
            self.todos.append(todo)
            self.todo_entry.delete(0, tk.END)  # Clear the entry field
            self.refresh_listbox()

    def remove_todo(self):
        """Remove the selected todo from the list."""
        try:
            index = self.todo_listbox.curselection()[0]  # Get selected index
            del self.todos[index]
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a todo to remove.")

    def refresh_listbox(self):
        """Refresh the contents of the listbox."""
        self.todo_listbox.delete(0, tk.END)  # Clear current items
        for todo in self.todos:
            self.todo_listbox.insert(tk.END, todo)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
