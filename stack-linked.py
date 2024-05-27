class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Stack is empty.")
            return None
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements:")
        current = self.top
        while current:
            print(current.data)
            current = current.next


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()  # Output: 4 3 2 1
    print("Popped item:", stack.pop())  # Output: Popped item: 4
    stack.display()  # Output: 3 2 1
    print("Peeked item:", stack.peek())  # Output: Peeked item: 3
