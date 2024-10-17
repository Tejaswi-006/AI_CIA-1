import math

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
estimate = {
    'X': 7,
    'Y': 6,
    'Z': 5,
    'V': 8,
    'W': 1,
    'U': 9,
    'T': 0
}

# AO* algorithm function
def ao_star_route(node, network, estimate, target, explored):
    # If node is the target, return 0 cost and the path as we have reached the target
    if node == target:
        return 0, [target]
    
    # If node is already explored, return a high cost to avoid cycles
    if node in explored:
        return math.inf, []
    
    explored.add(node)  # Mark the node as explored
    
    min_cost = math.inf
    best_path = []

    # Explore each OR subtree from the current node
    for neighbor, travel_cost in network[node].items():
        subtree_cost, subtree_path = ao_star_route(neighbor, network, estimate, target, explored)
        total_cost = travel_cost + subtree_cost  # Only consider the actual edge cost and subtree cost

        # Update if a cheaper subtree is found
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = [node] + subtree_path  # Add current node to the path
    
    explored.remove(node)  # Unmark the node after processing

    return min_cost, best_path

# Function to run the AO* algorithm
def run_ao_star_route(start_point, end_point):
    explored = set()  # Set to track explored nodes
    total_cost, route = ao_star_route(start_point, network, estimate, end_point, explored)
    return route, total_cost

# Test the AO* algorithm
start_point = 'X'
end_point = 'T'
route, total_cost = run_ao_star_route(start_point, end_point)

print("AO* Solution Route:", route)
print("Total Cost to Target:", total_cost)
