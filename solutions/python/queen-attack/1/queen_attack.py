class Queen:
    def __init__(self, row, column):
        self.check_position(row, column)

    def check_position(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def check_same_rc(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        elif self.row == another_queen.row:
            return True
        elif self.column == another_queen.column:
            return True 
        else:
            return False 
    
    def check_same_diags(self, another_queen, direction):
        row = self.row
        column = self.column
        if direction == 0: # lower right diagonal
            while row < 8 and column < 8:
                row += 1
                column += 1
                if row == another_queen.row and column == another_queen.column:
                    return True
            return False
        elif direction == 1: #upper right diagonal
            while row >=0 and column < 8:
                row -= 1
                column += 1
                if row == another_queen.row and column == another_queen.column:
                    return True
            return False
        elif direction == 2: #upper left diagonal
            while row >=0 and column >=0:
                row -=1
                column -= 1
                if row == another_queen.row and column == another_queen.column:
                    return True
            return False
        else: # lower left diagonal
            while row < 8 and column >=0:
                row += 1
                column -= 1
                if row == another_queen.row and column == another_queen.column:
                    return True   
            return False                             
    
    def can_attack(self, another_queen):
        # check if in the same row or column
        same_rc = self.check_same_rc(another_queen)
        if same_rc:
            return same_rc
        else:
            # now check diagonals
            if another_queen.row > self.row: # move down
                if another_queen.column > self.column:
                    return self.check_same_diags(another_queen, 0)
                else:
                    return self.check_same_diags(another_queen, 4)
            else: # move up
                if another_queen.column > self.column:
                    return self.check_same_diags(another_queen, 1)
                else:
                    return self.check_same_diags(another_queen, 2)




