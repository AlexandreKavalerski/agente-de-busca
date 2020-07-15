import SpaceTypes
class Cell():
    def __init__(self):
        self.type = SpaceTypes.TYPE_EMPTY
        self.color = SpaceTypes.EMPTY_COLOR
        
    def set_type(self, t, c):
        self.type = t
        self.color = c
        
    def __str__(self):
        return '[' + self.type + ']'
        
class Environment():
    def __init__(self, rows=8, cols=14):
        self.matrix = None
        self.rows = rows
        self.cols = cols
        
    def generate_environment(self, food_position, vehicle_position, quantity_of_obstacles=4):
        obstacles = 0
        # Gera a matrix com celulas vazias
        self.matrix = [[0] * self.cols for i in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = Cell()

        # Adiciona comida e veiculo na matriz (alterando o valor das celulas vazias que ocupam suas posicoes)
        self.matrix[food_position.row][food_position.col].set_type(SpaceTypes.TYPE_FOOD, SpaceTypes.FOOD_COLOR)
        self.matrix[vehicle_position.row][vehicle_position.col].set_type(SpaceTypes.TYPE_VEHICLE, SpaceTypes.VEHICLE_COLOR)
        
        while(obstacles < quantity_of_obstacles):
            random_col = int(random(self.cols))
            random_row = int(random(self.rows))
            if(self.matrix[random_row][random_col].type == SpaceTypes.TYPE_EMPTY):
                self.matrix[random_row][random_col].set_type(SpaceTypes.TYPE_OBSTACLE, SpaceTypes.OBSTACLE_COLOR)
                obstacles += 1
