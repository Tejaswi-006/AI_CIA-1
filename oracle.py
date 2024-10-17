import heapq

# Define the graph with weighted edges (costs)
network = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 2},  
    'E': {},  
    'G': {}   
}

# Function to find the least-cost path using a Dijkstra-like algorithm
def find_optimal_path(network, source, destination):
    # Priority queue (min-heap) to store the cost and path
    priority_queue = [(0, source, [source])]  # (current_cost, current_node, current_path)
    
    # Dictionary to track the minimum cost to reach each node
    shortest_path_costs = {node: float('inf') for node in network}
    shortest_path_costs[source] = 0
    
    while priority_queue:
        # Pop the node with the smallest cost
        current_cost, current_node, path = heapq.heappop(priority_queue)
        
        # If we've reached the destination, return the path and the cost
        if current_node == destination:
            return path, current_cost
        
        # Explore neighbors of the current node
        for adjacent_node, edge_cost in network[current_node].items():
            total_cost = current_cost + edge_cost
            
            # If this path to the adjacent node is cheaper, update the cost and add it to the queue
            if total_cost < shortest_path_costs[adjacent_node]:
                shortest_path_costs[adjacent_node] = total_cost
                heapq.heappush(priority_queue, (total_cost, adjacent_node, path + [adjacent_node]))
    
    # Return None if no path is found
    return None, float('inf')

# Test the least-cost oracle finding method
start_point = 'S'
end_point = 'G'

result_path, result_cost = find_optimal_path(network, start_point, end_point)

print("Optimal Path:", result_path)
print("Total Path Cost:", result_cost)
