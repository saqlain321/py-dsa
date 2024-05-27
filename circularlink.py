class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the circular linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself if it's the only node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        self.head = new_node

    # Function to insert a new node at the end of the circular linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself if it's the only node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Function to display the circular linked list
    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    cll.insert_at_beginning(4)
    cll.display()  # Output: 4 -> 1 -> 2 -> 3 ->
