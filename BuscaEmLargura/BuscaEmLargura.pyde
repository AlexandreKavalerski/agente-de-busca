from Grid import Grid

def setup():
    global grid
    size(700, 400)
    
    grid = Grid()
    
def draw():
    background(255)
    
    grid.display()
