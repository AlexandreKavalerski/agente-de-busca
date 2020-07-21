from Position import Position
import OperationTypes
import CellTypes

class Node:
    
    '''
    state: instancia da classe Position
    operation: string com um dos valores do arquivo OperationTypes
    gValue: valor correspondente a profundidade do no
    previousNode: instancia da classe Node
    '''
    def __init__(self, state, operation, gValue=0, previousNode=None):
        self.state = state
        self.operation = operation
        self.gValue = gValue
        self.hValue = None
        self.previousNode = previousNode
        
    def set_hValue(self, hValue):
        self.hValue = hValue
        
    def __str__(self):
        return 'Pos({}, {}) - Op: {} - Prev: {}'.format(self.state.row, self.state.col, self.operation, self.previousNode)
        
                        

def successor_function(node, space):
    children = []
    
    children.append(move_up(node))
    children.append(move_right(node, len(space[0])))
    children.append(move_down(node, len(space)))
    children.append(move_left(node))
    
    #Retorna somente os filhos validos
    children = list(filter(None, children))
    children = [c for c in children if space[c.state.row][c.state.col].type != CellTypes.TYPE_OBSTACLE]
    
    return children

def get_manhattan_distance(node, goal_position):
    dy = abs(node.state.row - goal_position.row)
    dx = abs(node.state.col - goal_position.col)
    return dx + dy
    
    
    
def move_up(node):
    new_state = node.state.move_up()
    
    return Node(new_state, OperationTypes.MOVE_UP, node.gValue+1, node) if new_state is not None else None
    
def move_right(node, col_limit):
    new_state = node.state.move_right(col_limit)
    
    return Node(new_state, OperationTypes.MOVE_RIGHT, node.gValue+1, node) if new_state is not None else None    

def move_down(node, row_limit):
    new_state = node.state.move_down(row_limit)
    
    return Node(new_state, OperationTypes.MOVE_DOWN, node.gValue+1, node) if new_state is not None else None

def move_left(node):
    new_state = node.state.move_left()
    
    return Node(new_state, OperationTypes.MOVE_LEFT, node.gValue+1, node) if new_state is not None else None
