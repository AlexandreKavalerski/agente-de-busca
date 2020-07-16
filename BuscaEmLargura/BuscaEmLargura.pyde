from Grid import Grid
from Environment import Environment
from Food import Food
from Vehicle import Vehicle

import CellTypes
import Search

def setup():
    global env, grid, food, vehicle
    size(700, 400)
    
    
    env = Environment(4,4)
    food = Food(3,3)
    vehicle = Vehicle(0,0)
    
    env.generate_environment(food.position, vehicle.position, 1)
    
    
    
    grid = Grid(env.matrix, env.rows, env.cols)
    
    solution = Search.search(vehicle.position, env.matrix[food.position.row][food.position.col], env.matrix, type='DFS')
    print(solution)
    
    
def draw():
    background(255)
    
    grid.display()
    
    
