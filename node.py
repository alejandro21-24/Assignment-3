class Node:
    """
    A single node used to build linked data structures (Stack, Queue).
    """

    def __init__(self, value):
        self.value = value
        self.next = None