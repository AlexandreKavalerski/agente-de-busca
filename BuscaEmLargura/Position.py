class Position():
    def __init__(self, line, col):
        self.line = line
        self.col = col
        
    def __eq__(self, other):
        return self.line == other.line and self.col == other.col
    
    def __str__(self):
        return '({}, {})'.format(self.line, self.col) 
        
