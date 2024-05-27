class Node:
    def __init__(self, col, val):
        self.col = col
        self.val = val
        self.next = None

class RowNode:
    def __init__(self, row):
        self.row = row
        self.head = None
        self.next_row = None

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.row_head = None

    def add_element(self, row, col, val):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Invalid row or column index.")
            return

        if val == 0:
            return

        new_node = Node(col, val)

        if not self.row_head:
            self.row_head = RowNode(row)
            self.row_head.head = new_node
            return

        prev_row = None
        current_row = self.row_head
        while current_row and current_row.row < row:
            prev_row = current_row
            current_row = current_row.next_row

        if current_row and current_row.row == row:
            prev_node = None
            current_node = current_row.head
            while current_node and current_node.col < col:
                prev_node = current_node
                current_node = current_node.next

            if current_node and current_node.col == col:
                current_node.val = val
            else:
                if not prev_node:
                    new_node.next = current_row.head
                    current_row.head = new_node
                else:
                    new_node.next = prev_node.next
                    prev_node.next = new_node
        else:
            new_row = RowNode(row)
            new_row.head = new_node
            if not prev_row:
                new_row.next_row = self.row_head
                self.row_head = new_row
            else:
                new_row.next_row = prev_row.next_row
                prev_row.next_row = new_row

    def display(self):
        if not self.row_head:
            print("Sparse Matrix is empty")
            return

        current_row = self.row_head
        for i in range(self.rows):
            if current_row and current_row.row == i:
                current_node = current_row.head
                for j in range(self.cols):
                    if current_node and current_node.col == j:
                        print(current_node.val, end=" ")
                        current_node = current_node.next
                    else:
                        print(0, end=" ")
                current_row = current_row.next_row
            else:
                for j in range(self.cols):
                    print(0, end=" ")
            print()


# Example usage:
if __name__ == "__main__":
    matrix = SparseMatrix(4, 5)
    matrix.add_element(0, 1, 3)
    matrix.add_element(0, 3, 7)
    matrix.add_element(1, 2, 4)
    matrix.add_element(2, 0, 9)
    matrix.add_element(2, 3, 5)
    matrix.display()
