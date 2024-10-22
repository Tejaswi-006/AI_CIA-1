import heapq

# Define the network graph
network = {
    'Source': {'Alpha': 6, 'Beta': 5},  
    'Alpha': {'Beta': 5, 'Delta': 1},  
    'Beta': {'Gamma': 8, 'Alpha': 6},
    'Gamma': {'Epsilon': 9},
    'Delta': {'Goal': 0},  
    'Epsilon': {},  
    'Goal': {}   
}

# Branch and Bound with Dead Horse Principle (Extended List)
def branch_and_bound_with_extended_list(network, start_node, goal_node):
    search_queue = [(0, start_node, [start_node])]  # Priority queue to store the current paths
    
    visited_nodes = {}  # Extended list to store the best costs for visited nodes
    
    optimal_cost = float('inf')
    optimal_path = None
    
    while search_queue:
    
        current_cost, current_node, current_path = heapq.heappop(search_queue)
        
        if current_node == goal_node and current_cost < optimal_cost:
            optimal_cost = current_cost
            optimal_path = current_path
        
        if current_node in visited_nodes and visited_nodes[current_node] <= current_cost:
            continue
        
        visited_nodes[current_node] = current_cost
        
        for neighbor_node, edge_cost in network[current_node].items():
            total_cost = current_cost + edge_cost
            
            if total_cost < optimal_cost:
                heapq.heappush(search_queue, (total_cost, neighbor_node, current_path + [neighbor_node]))
    
    return optimal_path, optimal_cost

start_node = 'Source'
goal_node = 'Goal'

solution_path, solution_cost = branch_and_bound_with_extended_list(network, start_node, goal_node)

print("Optimal Path Found (Branch and Bound with Extended List):", solution_path)
print("Total Path Cost:", solution_cost)
