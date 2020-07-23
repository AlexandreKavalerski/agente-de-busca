class Show:
    
    def __init__(self, x, y, value=0, pathCost='-'):
        self.position = PVector(x, y)
        self.score = value
        self.pathCost = pathCost
        
    def increaseScore(self):
        self.score += 1

    def setPathCost(self, pathCost):
        self.pathCost = pathCost

    def resetPathCost(self):
        self.pathCost = '-'
        
    def display(self):
        t = 'Comidas coletadas: {} \nCusto do caminho: {}'.format(self.score, self.pathCost)
        textSize(20)
        fill(50)
        text(t, self.position.x, self.position.y)