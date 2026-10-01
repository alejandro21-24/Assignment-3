# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # Queue was empty, so this node is both front and rear
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        removed_node = self.front
        self.front = removed_node.next

        if self.front is None:
            # Queue is now empty
            self.rear = None

        removed_node.next = None
        return removed_node.value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def print_queue(self):
        if self.front is None:
            print("[Queue is empty]")
            return

        current = self.front
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print("Front -> " + " -> ".join(values) + " -> Rear")


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)

            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()
            if name is not None:
                print(f"{name} has been helped.")
            else:
                print("No customers waiting.")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = queue.peek()
            if name is not None:
                print(f"Next customer: {name}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()