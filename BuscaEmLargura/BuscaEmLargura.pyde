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
    
    
    env = Environment()
    food = Food(5,8)
    vehicle = Vehicle(0,0)
    
    env.generate_environment(food.position, vehicle.position,10)
    
    
    
    grid = Grid(env.matrix, env.rows, env.cols)   
    
    
def draw():
    background(255)
    
    grid.display()
    
def keyPressed():
    if key == 'd':
        solution = vehicle.search_food(env.matrix, SearchTypes.DFS)
        print('Custo do caminho: ', solution.gValue)
        
    elif key == 'b':
        solution = vehicle.search_food(env.matrix, SearchTypes.BFS)
        print('Custo do caminho: ', solution.gValue)
    elif key == 'v':
        vehicle.run_solution(env.rows, env.cols, env)
        
    elif key == 'f':
        env.clear_visited_cells()
        env.update_food_position()
    elif key == 'c':
        env.clear_visited_cells()    
        
            
