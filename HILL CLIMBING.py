import random

# Define the graph and heuristics
network = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

# Heuristic values
heuristics = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

# Generate an initial solution using a greedy approach
def greedy_route(network, heuristics, start_node, end_node):
    current_node = start_node
    solution_path = [current_node]
    
    # Build the path by always selecting the neighbor with the lowest heuristic value
    while current_node != end_node:
        adjacent_nodes = network[current_node]
        if not adjacent_nodes:
            break
        next_node = min(adjacent_nodes, key=lambda n: heuristics[n])
        if next_node not in solution_path:  # Avoid cycles
            solution_path.append(next_node)
        current_node = next_node
    
    return solution_path

# Calculate the path cost based on heuristics
def calculate_cost(heuristics, solution_path):
    return sum([heuristics[node] for node in solution_path])

# Generate neighbors of a solution by swapping nodes
def swap_neighbors(solution_path):
    neighbor_solutions = []
    for i in range(1, len(solution_path) - 1):  # Exclude the start and end nodes from swapping
        for j in range(i + 1, len(solution_path) - 1):
            neighbor_solution = solution_path.copy()
            neighbor_solution[i], neighbor_solution[j] = neighbor_solution[j], neighbor_solution[i]  # Swap nodes
            neighbor_solutions.append(neighbor_solution)
    return neighbor_solutions

# Find the best neighbor based on the path cost
def find_best_neighbor(network, heuristics, current_solution):
    neighbor_solutions = swap_neighbors(current_solution)
    
    optimal_neighbor = current_solution
    optimal_cost = calculate_cost(heuristics, current_solution)
    
    for neighbor_solution in neighbor_solutions:
        neighbor_cost = calculate_cost(heuristics, neighbor_solution)
        if neighbor_cost < optimal_cost:
            optimal_cost = neighbor_cost
            optimal_neighbor = neighbor_solution
    
    return optimal_neighbor, optimal_cost

# Hill Climbing Algorithm
def hill_climbing_search(network, heuristics, start_node, end_node):
    # Generate an initial greedy solution
    current_solution = greedy_route(network, heuristics, start_node, end_node)
    current_cost = calculate_cost(heuristics, current_solution)
    
    while True:
        # Find the best neighbor
        optimal_neighbor, optimal_cost = find_best_neighbor(network, heuristics, current_solution)
        
        # If no improvement, break the loop
        if optimal_cost >= current_cost:
            print(f"Reached local optimum at {current_solution} with cost {current_cost}")
            break
        
        # Otherwise, move to the better neighbor
        current_solution = optimal_neighbor
        current_cost = optimal_cost
    
    return current_solution, current_cost

# Test the hill climbing algorithm
start_point = 'S'
goal_point = 'G'
final_solution, final_cost = hill_climbing_search(network, heuristics, start_point, goal_point)

print("Final Solution Path:", final_solution)
print("Final Path Cost:", final_cost)
