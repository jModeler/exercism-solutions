class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        self.matrix = [row.split(" ") for row in self.matrix]

    def row(self, index):
        row = self.matrix[index - 1]
        row = list(map(int, row))
        return row

    def column(self, index):
        col = []
        for row in self.matrix:
            val = int(row[index-1])
            col.append(val)
        return col

        
