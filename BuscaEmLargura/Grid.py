import SpaceTypes

class Grid:
    
    def __init__(self, matrix, rows, cols, spacing=49):
        self.spacing = min(width/cols, height/rows)
        self.cols = cols
        self.rows = rows
        self.matrix = matrix
        
        
        
    def display(self):
        
        # Preenche um grid na tela tendo como referencia a matriz que representa o ambiente
        for i in range(self.rows):
            for j in range(self.cols):
                x = j * self.spacing
                y = i * self.spacing               
                
                # Preenche o a celula no grid com a cor do seu tipo
                fill(self.matrix[i][j].color)
                stroke(0)
                rect(x, y, self.spacing, self.spacing)
