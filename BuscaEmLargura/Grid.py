class Grid:
    
    def __init__(self, spacing=49):
        self.spacing = spacing
        self.cols = width/spacing
        self.rows = height/spacing
        
        
    def display(self):
            
        for i in range(self.cols):
            for j in range(self.rows):
                x = i * self.spacing
                y = j * self.spacing
                
                fill(255)
                stroke(0)
                rect(x, y, self.spacing, self.spacing)
