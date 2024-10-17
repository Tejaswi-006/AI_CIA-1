import heapq

# Define the network with weighted edges (costs)
network = {
    'S': {'A': 6, 'B': 5},  
    'A': {'B': 5, 'D': 1},  
    'B': {'C': 8, 'A': 6},
    'C': {'E': 9},
    'D': {'G': 0},  
    'E': {},  
    'G': {}   
}

# Define the heuristic values (estimated cost to reach the target)
heuristics = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 8,
    'D': 1,
    'E': 9,
    'G': 0
}

# Best First Search (BFS) Algorithm with cost calculation
def best_first_search(source, target, network, heuristics):
    # Priority queue to store (heuristic_value, current_node, path, cumulative_cost)
    queue = []
    heapq.heappush(queue, (heuristics[source], source, [source], 0))
    
    # Set of explored nodes
    explored_nodes = set()
    
    while queue:
        # Pop the node with the lowest heuristic value
        h_val, current_node, current_route, accumulated_cost = heapq.heappop(queue)
        
        # If the target is reached, return the route and total cost
        if current_node == target:
            return current_route, accumulated_cost
        
        # Mark the current node as explored
        explored_nodes.add(current_node)
        
        # Explore the adjacent nodes
        for adjacent_node, edge_cost in network[current_node].items():
            if adjacent_node not in explored_nodes:
                # Calculate the new cumulative cost to the adjacent node
                total_cost = accumulated_cost + edge_cost
                # Push the adjacent node to the priority queue with its heuristic value and updated route and cost
                heapq.heappush(queue, (heuristics[adjacent_node], adjacent_node, current_route + [adjacent_node], total_cost))
    
    return None, None  # In case no route is found

# Run Best First Search
source_node = 'S'
target_node = 'G'
solution_route, total_route_cost = best_first_search(source_node, target_node, network, heuristics)

print("Best First Search Solution Path:", solution_route)
print("Total Cost:", total_route_cost)
