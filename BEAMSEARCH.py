import heapq

# Define the network graph
network = {
    'Source': {'Alpha': 6, 'Beta': 5},  
    'Alpha': {'Beta': 5, 'Delta': 1},  
    'Beta': {'Gamma': 8, 'Alpha': 6},
    'Gamma': {'Epsilon': 9},
    'Delta': {'Goal': 2},  
    'Epsilon': {},  
    'Goal': {}   
}

# Heuristic values for the nodes
estimated_cost = {
    'Source': 7,
    'Alpha': 6,
    'Beta': 5,
    'Gamma': 8,
    'Delta': 1,
    'Epsilon': 9,
    'Goal': 0
}

# Function to get the neighbors (successors) of the current node
def get_neighbors(network, node):
    return network[node].keys()

# Beam Search Algorithm
def beam_search(network, estimated_cost, start_node, goal_node, beam_width=2):
    beam = [(estimated_cost[start_node], [start_node])]  # Start with the initial node in the beam
    
    while beam:
        new_beam = []
        
        for cost, path in beam:
            current_node = path[-1]
            
            if current_node == goal_node:
                return path, cost  # Return the path if the goal node is found
            
            for neighbor_node in get_neighbors(network, current_node):
                if neighbor_node not in path:  # Avoid cycles
                    new_path = path + [neighbor_node]
                    new_cost = cost + estimated_cost[neighbor_node]  # Update the cost
                    
                    new_beam.append((new_cost, new_path))
        
        beam = heapq.nsmallest(beam_width, new_beam, key=lambda x: x[0])  # Keep the top beam_width paths
        
    return None, float('inf')  # Return no solution if the goal node isn't found

start_node = 'Source'
goal_node = 'Goal'
solution, cost = beam_search(network, estimated_cost, start_node, goal_node, beam_width=2)

print("Beam Search Solution Path:", solution)
print("Beam Search Path Cost:", cost)
