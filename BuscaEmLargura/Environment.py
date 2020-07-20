import CellTypes
class Cell():
    def __init__(self):
        self.type = CellTypes.TYPE_EMPTY
        self.color = CellTypes.EMPTY_COLOR
        self.visited = False
        
    def set_type(self, t, c):
        self.type = t
        self.color = c
        
    def __str__(self):
        return '[' + self.type + ']'
    
    def set_visited(self):
        self.visited = True
        self.color = CellTypes.VISITED_COLOR
    
    def set_solution(self):
        self.visited = True
        self.color = CellTypes.SOLUTION_COLOR
        
class Environment():
    def __init__(self, rows=8, cols=14):
        self.matrix = None
        self.rows = rows
        self.cols = cols
        
    def clear_visited_cells(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j].visited:    
                    self.matrix[i][j].visited = False
                    self.matrix[i][j].color = CellTypes.EMPTY_COLOR
        
    def generate_environment(self, food_position, vehicle_position, quantity_of_obstacles=4):
        obstacles = 0
        # Gera a matrix com celulas vazias
        self.matrix = [[0] * self.cols for i in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell()

        # Adiciona comida e veiculo na matriz (alterando o valor das celulas vazias que ocupam suas posicoes)
        self.matrix[food_position.row][food_position.col].set_type(CellTypes.TYPE_FOOD, CellTypes.FOOD_COLOR)
        self.matrix[vehicle_position.row][vehicle_position.col].set_type(CellTypes.TYPE_VEHICLE, CellTypes.VEHICLE_COLOR)
        
        while(obstacles < quantity_of_obstacles):
            random_col = int(random(self.cols))
            random_row = int(random(self.rows))
            if(self.matrix[random_row][random_col].type == CellTypes.TYPE_EMPTY):
                self.matrix[random_row][random_col].set_type(CellTypes.TYPE_OBSTACLE, CellTypes.OBSTACLE_COLOR)
                obstacles += 1
    
    def update_vehicle_position(self, vehicle_position):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j].type == CellTypes.TYPE_VEHICLE:
                    self.matrix[i][j] = Cell()
                    self.matrix[i][j].set_solution()
                    
        self.matrix[vehicle_position.row][vehicle_position.col].set_type(CellTypes.TYPE_VEHICLE, CellTypes.VEHICLE_COLOR)
        
        
                
