from Position import Position
from Search import search, visit_solution
from Environment import Cell

import CellTypes

class Vehicle():

    def __init__(self, row, col):
        self.position = Position(row, col)
        self.solution = None
        
    def search_food(self, matrix, search_type):
        cell_food = Cell()
        cell_food.set_type(CellTypes.TYPE_FOOD, CellTypes.FOOD_COLOR)
        
        return search(self.position, cell_food, matrix, search_type)
