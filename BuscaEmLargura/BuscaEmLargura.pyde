import sys
sys.path.append("../utils")

from Grid import Grid
from Environment import Environment
from Food import Food
from Vehicle import Vehicle

import CellTypes
import SearchTypes
import Search

def setup():
    global env, grid, food, vehicle
    global timeToWait, lastTime, foundSolution  
    timeToWait = 2000
    foundSolution = False
    
    size(700, 400)
    
    
    env = Environment()
    food = Food(5,8)
    vehicle = Vehicle(0,0)
    
    env.generate_environment(food.position, vehicle.position,10)
    
    
    
    grid = Grid(env.matrix, env.rows, env.cols)   
    
    lastTime = millis()
    
    
def draw():
    background(255)
    grid.display()
    
    global timeToWait, lastTime, foundSolution
    if( millis() - lastTime > timeToWait and not foundSolution):      
        solution = vehicle.search_food(env, SearchTypes.BFS)
        print('Custo do caminho: ', solution.gValue)
        vehicle.run_solution(env.rows, env.cols, env)
        
        lastTime = millis()
        foundSolution = True
    elif( millis() - lastTime > timeToWait and foundSolution):    
        env.clear_visited_cells()
        env.update_food_position()
        lastTime = millis()
        foundSolution = False
            
            
