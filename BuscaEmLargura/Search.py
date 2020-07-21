from Node import Node, successor_function, get_manhattan_distance
import OperationTypes
import CellTypes
import SearchTypes

'''
initial_state: instancia da classe Position
goal_state: instancia da classe Cell() //corresponde a celula referente a comida
env: corresponde a uma instancia do objeto Environment
type: indica o tipo de busca a ser realizada // 'DFS' | 'BFS' | ...  
'''
def search(initial_state, goal_state, env, type):
    first_node = Node(initial_state, OperationTypes.NONE)
    frontier = [first_node]
    
    if type == SearchTypes.DFS:
        return dfs(goal_state, frontier, env.matrix)
    elif type == SearchTypes.BFS:
        return bfs(goal_state, frontier, env.matrix)
    elif type == SearchTypes.UCS:
        return ucs(goal_state, frontier, env.matrix)
    elif type == SearchTypes.GRE:
        return greedy(goal_state, frontier, env)
    elif type == SearchTypes.STA:
        return a_star(goal_state, frontier, env)

def dfs(goal, frontier, space):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while space[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, space)
        for c in children:            
            if c.state not in visited_states:
                frontier.insert(0,c)
                if space[c.state.row][c.state.col].type == CellTypes.TYPE_EMPTY:
                    space[c.state.row][c.state.col].set_expanded()
                
            if space[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                space[actual_node.state.row][actual_node.state.col].set_visited()
            visited_states.append(actual_node.state)

        actual_node = frontier.pop(0)
    return actual_node

def bfs(goal, frontier, space):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while space[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, space)
        
        for c in children:            
            if c.state not in visited_states:
                frontier.append(c)
                if space[c.state.row][c.state.col].type == CellTypes.TYPE_EMPTY:
                    space[c.state.row][c.state.col].set_expanded()
                
            if space[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                space[actual_node.state.row][actual_node.state.col].set_visited()
                
            visited_states.append(actual_node.state)
        actual_node = frontier.pop(0)
    return actual_node


def ucs(goal, frontier, space):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while space[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, space)
        
        for c in children:            
            if c.state not in visited_states:
                frontier.append(c)
                if space[c.state.row][c.state.col].type == CellTypes.TYPE_EMPTY:
                    space[c.state.row][c.state.col].set_expanded()
                
            if space[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                space[actual_node.state.row][actual_node.state.col].set_visited()
                
            visited_states.append(actual_node.state)
        frontier.sort(key=lambda node: node.gValue)
        actual_node = frontier.pop(0)
    return actual_node

def greedy(goal, frontier, env):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while env.matrix[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, env.matrix)
        
        for c in children:            
            if c.state not in visited_states:
                frontier.append(c)
                c.set_hValue(get_manhattan_distance(c, env.food_position))
                if env.matrix[c.state.row][c.state.col].type == CellTypes.TYPE_EMPTY:
                    env.matrix[c.state.row][c.state.col].set_expanded()
                
            if env.matrix[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                env.matrix[actual_node.state.row][actual_node.state.col].set_visited()
                
            visited_states.append(actual_node.state)
        frontier.sort(key=lambda node: node.hValue)
        actual_node = frontier.pop(0)
    return actual_node

def a_star(goal, frontier, env):
    visited_states = []
    actual_node = frontier.pop(0)
    
    while env.matrix[actual_node.state.row][actual_node.state.col].type != goal.type:
        children = successor_function(actual_node, env.matrix)
        
        for c in children:            
            if c.state not in visited_states:
                frontier.append(c)
                c.set_hValue(get_manhattan_distance(c, env.food_position))
                if env.matrix[c.state.row][c.state.col].type == CellTypes.TYPE_EMPTY:
                    env.matrix[c.state.row][c.state.col].set_expanded()
                
            if env.matrix[actual_node.state.row][actual_node.state.col].type == CellTypes.TYPE_EMPTY:
                env.matrix[actual_node.state.row][actual_node.state.col].set_visited()
                
            visited_states.append(actual_node.state)
        frontier.sort(key=lambda node: (node.hValue + node.gValue))
        actual_node = frontier.pop(0)
    return actual_node

def visit_solution(node, space):
    if node.previousNode is not None:
        if space[node.state.row][node.state.col].type == CellTypes.TYPE_EMPTY:
            space[node.state.row][node.state.col].set_solution()
        return visit_solution(node.previousNode, space)
    return True
    
