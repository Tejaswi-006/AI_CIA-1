import heapq

# Define the network with weighted edges (costs)
network = {
    'X': {'Y': 6, 'Z': 5},  
    'Y': {'Z': 5, 'W': 1},  
    'Z': {'V': 8, 'Y': 6},
    'V': {'U': 9},
    'W': {'T': 0},  
    'U': {},  
    'T': {}   
}

# Branch and Bound Algorithm
def branch_and_bound(network, source, target):
    # Priority queue (min-heap) to store paths with their cost
    queue = [(0, source, [source])]  # (cost, current_node, path)
    
    # Initialize the best known cost to infinity
    optimal_cost = float('inf')
    optimal_path = None
    
    while queue:
        # Pop the path with the smallest cost
        current_cost, current_node, current_path = heapq.heappop(queue)
        
        # If we have reached the target and the cost is lower than the best known cost
        if current_node == target and current_cost < optimal_cost:
            optimal_cost = current_cost
            optimal_path = current_path
        
        # Explore neighbors of the current node
        for neighbor, edge_cost in network[current_node].items():
            total_cost = current_cost + edge_cost
            
            # Only add the neighbor to the queue if its cost is less than the best known cost
            if total_cost < optimal_cost:
                heapq.heappush(queue, (total_cost, neighbor, current_path + [neighbor]))
    
    return optimal_path, optimal_cost

# Test the Branch and Bound algorithm
source_node = 'X'
target_node = 'T'

solution_route, total_cost = branch_and_bound(network, source_node, target_node)

print("Best Path Found (Branch and Bound):", solution_route)
print("Total Path Cost:", total_cost)
