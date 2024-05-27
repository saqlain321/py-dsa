class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
current = head
for i in range(2, 6):
    current.next = Node(i)
    current = current.next

print("Original Linked List:")
current = head
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print("None")

head = reverse_linked_list(head)

print("Reversed Linked List:")
current = head
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print("None")
