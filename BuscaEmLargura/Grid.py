import SpaceTypes

class Grid:
    
    def __init__(self, matrix, rows, cols, spacing=49):
        self.spacing = min(width/cols, height/rows)
        self.cols = cols
        self.rows = rows
        self.matrix = matrix
        
        
        
    def display(self):
        
        # Preenche um grid na tela tendo como referencia a matriz que representa o ambiente
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                x = i * self.spacing
                y = j * self.spacing               
                
                # Preenche o a celula no grid com a cor do seu tipo
                fill(self.matrix[i][j].color)
                stroke(0)
                rect(x, y, self.spacing, self.spacing)
