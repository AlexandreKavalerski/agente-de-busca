from Position import Position
import OperationTypes
import SpaceTypes

class Node:
    
    '''
    state: instancia da classe Position
    operation: string com um dos valores do arquivo OperationTypes
    previousNode: instancia da classe Node
    '''
    def __init__(self, state, operation, previousNode=None):
        self.state = state
        self.operation = operation
        self.previousNode = previousNode
        
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
    children = [c for c in children if space[c.state.row][c.state.col].type != SpaceTypes.TYPE_OBSTACLE]
    
    return children
    
    
def move_up(node):
    new_line = node.state.row - 1
    new_col = node.state.col
    
    new_state = Position(new_col, new_line)
    return Node(new_state, OperationTypes.MOVE_UP, node) if new_line >= 0 else None
    
def move_right(node, col_limit):
    new_line = node.state.row
    new_col = node.state.col + 1
    
    new_state = Position(new_col, new_line)
    return Node(new_state, OperationTypes.MOVE_RIGHT, node) if new_col < col_limit else None    

def move_down(node, line_limit):
    new_line = node.state.row + 1
    new_col = node.state.col
    
    new_state = Position(new_col, new_line)
    return Node(new_state, OperationTypes.MOVE_DOWN, node) if new_line < line_limit else None

def move_left(node):
    new_line = node.state.row
    new_col = node.state.col - 1
    
    new_state = Position(new_col, new_line)
    return Node(new_state, OperationTypes.MOVE_LEFT, node) if new_col >= 0 else None
