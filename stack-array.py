class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Stack is full.")
            return
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Stack is empty.")
            return None
        popped_item = self.stack.pop()
        self.top -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements:")
        for i in range(self.top, -1, -1):
            print(self.stack[i])


# Example usage:
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()  # Output: 4 3 2 1
    print("Popped item:", stack.pop())  # Output: Popped item: 4
    stack.display()  # Output: 3 2 1
    print("Peeked item:", stack.peek())  # Output: Peeked item: 3
    print("Size of stack:", stack.size())  # Output: Size of stack: 3
