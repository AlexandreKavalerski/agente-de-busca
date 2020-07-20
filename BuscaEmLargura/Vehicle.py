from Position import Position
from Search import search, visit_solution
from Environment import Cell

import CellTypes
import OperationTypes

class Vehicle():

    def __init__(self, row, col):
        self.position = Position(row, col)
        self.solution = None
        
    '''
    direction: indica a direcao a qual o veiculo devera se mover (o valor deve ser uma das constantes em OperationTypes.py) // 'up' | 'right' | ... 
    '''
    def move(self, direction, limit=None):
        if direction == OperationTypes.MOVE_UP:
            new_position = self.position.move_up()
            if new_position is not None:
                self.position = new_position
        elif direction == OperationTypes.MOVE_RIGHT:
            new_position = self.position.move_right(limit)
            if new_position is not None:
                self.position = new_position
        elif direction == OperationTypes.MOVE_DOWN:
            new_position = self.position.move_down(limit)
            if new_position is not None:
                self.position = new_position
        elif direction == OperationTypes.MOVE_LEFT:
            new_position = self.position.move_left()
            if new_position is not None:
                self.position = new_position        
        
    
    '''
    matrix: corresponde apenas a uma matriz de objetos do tipo Cell
    search_type: indica o tipo de busca a ser realizada // 'DFS' | 'BFS' | ...
    '''    
    def search_food(self, matrix, search_type):
        cell_food = Cell()
        cell_food.set_type(CellTypes.TYPE_FOOD, CellTypes.FOOD_COLOR)
        
        return search(self.position, cell_food, matrix, search_type)
