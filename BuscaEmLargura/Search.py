from Node import Node, successor_function
import OperationTypes

'''
initial_state: instancia da classe Position
goal_state: instancia da classe Cell() //corresponde a celula referente a comida
space: corresponde apenas a uma matriz de objetos do tipo Cell
type: indica o tipo de busca a ser realizada // 'DFS' | 'BFS' | ...  
'''
def search(initial_state, goal_state, space, type='DFS'):
    first_node = Node(initial_state, OperationTypes.NONE)
    frontier = [first_node]
    
    dfs(goal_state, frontier, space)

def dfs(goal, frontier, space):
    visited_states = []
    actual_node = frontier.pop(0)
    
    
    while space[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, space)
        print('len: {}'.format(len(children)))
        for c in children:            
            if c.state not in visited_states:
                frontier.append(c) 
                visited_states.append(c.state)
        
        actual_node = frontier.pop()
        print(len(frontier))
    
    
