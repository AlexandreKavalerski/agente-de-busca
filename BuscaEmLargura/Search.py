from Node import Node, successor_function
import OperationTypes
import CellTypes

'''
initial_state: instancia da classe Position
goal_state: instancia da classe Cell() //corresponde a celula referente a comida
space: corresponde apenas a uma matriz de objetos do tipo Cell
type: indica o tipo de busca a ser realizada // 'DFS' | 'BFS' | ...  
'''
def search(initial_state, goal_state, space, type='DFS'):
    first_node = Node(initial_state, OperationTypes.NONE)
    frontier = [first_node]
    
    return dfs(goal_state, frontier, space)

def dfs(goal, frontier, space):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while space[actual_node.state.row][actual_node.state.col].type != goal.type:
        print(actual_node)
        children = successor_function(actual_node, space)
        print('filhos: {}'.format(len(children)))
        for c in children:            
            if c.state not in visited_states:
                frontier.insert(0,c)
                
            if space[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                space[actual_node.state.row][actual_node.state.col].set_visited()
            visited_states.append(actual_node.state)

        print('-----------------')
        for n in frontier: print(n.state)
        print('-----------------')        
        actual_node = frontier.pop(0)
    return actual_node

def visit_solution(node, space):
    if node.previousNode is not None:
        if space[node.state.row][node.state.col].type == CellTypes.TYPE_EMPTY:
            space[node.state.row][node.state.col].set_solution()
        return visit_solution(node.previousNode, space)
    return True
    
