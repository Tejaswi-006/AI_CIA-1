def depth_first_search(network, source, target, explored=None, route=None):
    if explored is None:
        explored = set()  # Initialize the explored set
    if route is None:
        route = []  # Initialize route list to track the current path
    
    explored.add(source)  # Mark the current node as explored
    route.append(source)  # Add current node to the route
    print(f"Exploring: {source}")

    if source == target:
        print(f"Target {target} found!")
        print("Route:", " -> ".join(route))
        return True  # Stop the search when target is found

    # Explore the neighbors of the current node
    for adjacent_node in network[source]:
        if adjacent_node not in explored:
            if depth_first_search(network, adjacent_node, target, explored, route):  # Recursively visit adjacent nodes
                return True  # Return True if the target is found in the adjacent node's path

    route.pop()  # Backtrack: remove the current node from the route
    return False  # Return False if the target was not found


# Network structure with S as the source and G as the target
network = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E'],
    'D': ['G'],
    'E': [],   # E is a dead end
    'G': []    # G is the target
}

# Test DFS with 'S' as the source and 'G' as the target
depth_first_search(network, 'S', 'G')
