from node import Node


class Stack:
    """
    A LIFO (Last In, First Out) stack implemented with linked Nodes.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """Add a new Node with the given value to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove the Node at the top of the stack and return its value."""
        if self.top is None:
            return None
        removed_node = self.top
        self.top = removed_node.next
        removed_node.next = None
        return removed_node.value

    def peek(self):
        """Return the value at the top of the stack without removing it."""
        if self.top is None:
            return None
        return self.top.value

    def print_stack(self):
        """Print the current stack contents, top to bottom."""
        if self.top is None:
            print("[Stack is empty]")
            return

        current = self.top
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print("Top -> " + " -> ".join(values) + " -> Bottom")


def run_undo_redo_cli():
    undo_stack = Stack()
    redo_stack = Stack()

    menu = """
--- Undo / Redo System ---
1. Perform Action
2. Undo
3. Redo
4. View Undo Stack
5. View Redo Stack
6. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            action = input("Enter the action to perform: ").strip()
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo history on a new action
            print(f'Action "{action}" performed.')

        elif choice == "2":
            value = undo_stack.pop()
            if value is not None:
                redo_stack.push(value)
                print(f'Undid: "{value}"')
            else:
                print("No actions to undo")

        elif choice == "3":
            value = redo_stack.pop()
            if value is not None:
                undo_stack.push(value)
                print(f'Redid: "{value}"')
            else:
                print("No actions to redo")

        elif choice == "4":
            print("Undo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("Redo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    run_undo_redo_cli()