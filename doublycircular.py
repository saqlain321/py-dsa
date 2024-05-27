class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the circular doubly linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node
            self.head = new_node

    # Function to insert a new node at the end of the circular doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last_node = self.head.prev
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node
            last_node.next = new_node

    # Function to display the circular doubly linked list in forward direction
    def display_forward(self):
        if not self.head:
            print("Circular Doubly Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print()

    # Function to display the circular doubly linked list in backward direction
    def display_backward(self):
        if not self.head:
            print("Circular Doubly Linked List is empty")
            return
        current = self.head.prev
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.head.prev:
                break
        print()


# Example usage:
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.insert_at_beginning(1)
    cdll.insert_at_beginning(2)
    cdll.insert_at_end(3)
    cdll.display_forward()  # Output: 2 <-> 1 <-> 3 <-> 
    cdll.display_backward()  # Output: 3 <-> 1 <-> 2 <-> 
