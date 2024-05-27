class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the doubly linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Function to insert a new node at the end of the doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    # Function to display the doubly linked list (forward)
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Function to display the doubly linked list (backward)
    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.insert_at_end(3)
    dll.display_forward()  # Output: 2 <-> 1 <-> 3 <-> None
    dll.display_backward()  # Output: 3 <-> 1 <-> 2 <-> None
