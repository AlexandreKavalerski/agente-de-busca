class Position():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __str__(self):
        return '({}, {})'.format(self.row, self.col) 
        
        
    def move_up(self):
        new_row = self.row - 1
        new_col = self.col
        
        return Position(new_row, new_col) if new_row >= 0 else None
    
    def move_right(self, col_limit):
        new_row = self.row
        new_col = self.col + 1
        
        return Position(new_row, new_col) if new_col < col_limit else None    
    
    def move_down(self, row_limit):
        new_row = self.row + 1
        new_col = self.col
        
        return Position(new_row, new_col) if new_row < row_limit else None
    
    def move_left(self):
        new_row = self.row
        new_col = self.col - 1
        
        return Position(new_row, new_col) if new_col >= 0 else None
