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

# Define the heuristic values (estimated cost to reach target)
estimate = {
    'X': 7,
    'Y': 6,
    'Z': 5,
    'V': 8,
    'W': 1,
    'U': 9,
    'T': 0
}

def a_star_route(network, estimate, source, target):
    # Priority queue to store (f_cost, g_cost, current_node, route)
    priority_queue = [(estimate[source], 0, source, [source])]
    
    # Dictionary to track the cost to reach each node
    explored = {}
    
    while priority_queue:
        # Pop the node with the lowest f(n) value
        f_cost, g_cost, current_node, route = heapq.heappop(priority_queue)
        
        # If we've reached the target, return the solution
        if current_node == target:
            return route, g_cost
        
        # If this node has already been visited with a lower cost, skip it
        if current_node in explored and explored[current_node] <= g_cost:
            continue
        
        # Mark this node as visited
        explored[current_node] = g_cost
        
        # Explore the neighbors of the current node
        for neighbor, travel_cost in network[current_node].items():
            total_cost = g_cost + travel_cost  # g(n)
            f_neighbor_cost = total_cost + estimate[neighbor]  # f(n) = g(n) + h(n)
            
            # Add the neighbor to the priority queue
            heapq.heappush(priority_queue, (f_neighbor_cost, total_cost, neighbor, route + [neighbor]))
    
    return None, float('inf')  # If no path is found

# Test the A* algorithm
source_node = 'X'
target_node = 'T'

optimal_route, optimal_cost = a_star_route(network, estimate, source_node, target_node)

print("A* Algorithm Optimal Route:", optimal_route)
print("Total Route Cost:", optimal_cost)
