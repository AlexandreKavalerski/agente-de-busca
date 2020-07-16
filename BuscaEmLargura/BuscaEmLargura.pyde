from Grid import Grid
from Environment import Environment
from Food import Food
from Vehicle import Vehicle

import CellTypes
import SearchTypes
import Search

def setup():
    global env, grid, food, vehicle
    size(700, 400)
    
    
    env = Environment(4, 4)
    food = Food(3,3)
    vehicle = Vehicle(0,0)
    
    env.generate_environment(food.position, vehicle.position)
    
    
    
    grid = Grid(env.matrix, env.rows, env.cols)   
    
    
def draw():
    background(255)
    
    grid.display()
    
def keyPressed():
    if key == 'd':
        solution = Search.search(vehicle.position, env.matrix[food.position.row][food.position.col], env.matrix, SearchTypes.DFS)
    elif key == 'b':
        solution = Search.search(vehicle.position, env.matrix[food.position.row][food.position.col], env.matrix, SearchTypes.BFS)
    elif key == 'c':
        env.clear_visited_cells()    
        
            
