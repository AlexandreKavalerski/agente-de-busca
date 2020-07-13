from Grid import Grid
from Environment import Environment
from Food import Food
from Vehicle import Vehicle

def setup():
    global env, grid, food, vehicle
    size(700, 400)
    
    
    env = Environment()
    food = Food(7,10)
    vehicle = Vehicle(0,0)
    
    env.generate_environment(food.position, vehicle.position)
    
    grid = Grid(env.matrix, env.rows, env.cols)
    
def draw():
    background(255)
    
    grid.display()
