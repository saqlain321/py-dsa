class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.triplets = []

    def add_element(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Invalid row or column index.")
            return
        if value != 0:
            self.triplets.append((row, col, value))

    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                found = False
                for triplet in self.triplets:
                    if triplet[0] == i and triplet[1] == j:
                        found = True
                        print(triplet[2], end=" ")
                        break
                if not found:
                    print(0, end=" ")
            print()


# Example usage:
if __name__ == "__main__":
    matrix = SparseMatrix(4, 5)
    matrix.add_element(0, 1, 3)
    matrix.add_element(0, 3, 7)
    matrix.add_element(1, 2, 4)
    matrix.add_element(2, 0, 9)
    matrix.display()
