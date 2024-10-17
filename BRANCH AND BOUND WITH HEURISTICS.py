import heapq

# Define the network with weighted edges (costs)
network = {
    'X': {'Y': 6, 'Z': 5},  
    'Y': {'Z': 5, 'W': 1},  
    'Z': {'V': 8, 'Y': 6},
    'V': {'U': 9},
    'W': {'T': 2},  
    'U': {},  
    'T': {}   
}

# Define the heuristic values (estimated cost to reach target)
estimates = {
    'X': 7,
    'Y': 6,
    'Z': 5,
    'V': 8,
    'W': 1,
    'U': 9,
    'T': 0
}

# Branch and Bound with Heuristics
def branch_and_bound_with_heuristic(network, estimates, source, target):
    # Priority queue (min-heap) to store paths with their f(n) cost (g(n) + h(n))
    queue = [(0 + estimates[source], 0, source, [source])]  # (f_cost, g_cost, current_node, path)
    
    # Visited nodes with the minimum cost they were visited at
    visited = {}
    
    # Initialize the best known cost to infinity
    optimal_cost = float('inf')
    optimal_path = None
    
    while queue:
        # Pop the path with the smallest f(n) cost
        f_cost, current_cost, current_node, route = heapq.heappop(queue)
        
        # If we have reached the target and the cost is lower than the best known cost
        if current_node == target and current_cost < optimal_cost:
            optimal_cost = current_cost
            optimal_path = route
            continue  # Continue searching for potentially better routes
        
        # Check if this node was visited with a lower or equal cost before
        if current_node in visited and visited[current_node] <= current_cost:
            continue  # Skip as we've visited it with a better or equal cost
        
        # Update the visited nodes with the new minimum cost
        visited[current_node] = current_cost
        
        # Explore neighbors of the current node
        for neighbor, edge_cost in network[current_node].items():
            total_cost = current_cost + edge_cost
            f_neighbor_cost = total_cost + estimates[neighbor]
            
            # Only add the neighbor if its total cost is less than the best known cost
            if total_cost < optimal_cost:
                heapq.heappush(queue, (f_neighbor_cost, total_cost, neighbor, route + [neighbor]))
    
    return optimal_path, optimal_cost

# Test the Branch and Bound with Heuristics
source_node = 'X'
target_node = 'T'

solution_route, total_cost = branch_and_bound_with_heuristic(network, estimates, source_node, target_node)

print("Best Route Found (Branch and Bound with Heuristics):", solution_route)
print("Total Route Cost:", total_cost)
