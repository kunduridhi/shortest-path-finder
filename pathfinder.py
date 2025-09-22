from queue import Queue

# Maze representation (ridhi)
ridhi = [
    ["#", "#", "#", "#", "S", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", " ", " ", "#", "#", " ", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "X", "#", "#", "#", "#", "#", "#", "#"]
]

# Display the maze
def display_ridhi(ridhi):
    for row in ridhi:
        print(" ".join(row))

# Find the start/end node
def find_node(ridhi, node):
    for row in range(len(ridhi)):
        for col in range(len(ridhi[0])):
            if ridhi[row][col] == node:
                return (row, col)

# Transform maze to graph
def transform_to_graph(ridhi):
    graph = {}
    for row in range(len(ridhi)):
        for col in range(len(ridhi[0])):
            if ridhi[row][col] != '#':
                adj_nodes = []
                if row+1 < len(ridhi) and ridhi[row+1][col] != '#':
                    adj_nodes.append((row+1, col))
                if row-1 >= 0 and ridhi[row-1][col] != '#':
                    adj_nodes.append((row-1, col))
                if col+1 < len(ridhi[0]) and ridhi[row][col+1] != '#':
                    adj_nodes.append((row, col+1))
                if col-1 >= 0 and ridhi[row][col-1] != '#':
                    adj_nodes.append((row, col-1))
                graph[(row, col)] = adj_nodes
    return graph

# BFS Solver
def solve_ridhi(ridhi, ridhi_graph, start_node, end_node):
    visited = []
    start_path = [start_node]
    q = Queue()
    q.put(start_path)

    while not q.empty():
        path = q.get()
        neighbours = ridhi_graph[path[-1]]

        for node in neighbours:
            if node == end_node:
                final_path = path + [node]
                # Mark path in maze
                for (row, col) in final_path:
                    if ridhi[row][col] not in ['S', 'X']:
                        ridhi[row][col] = '*'
                # Show path details
                print("\nShortest Path Found ✅")
                print("Path Coordinates:", final_path)
                print("Path Length:", len(final_path)-1, "steps")
                return ridhi
            
            if node not in visited:
                visited.append(node)
                new_path = path + [node]
                q.put(new_path)

# Run the solver
start_node = find_node(ridhi, 'S')
end_node = find_node(ridhi, 'X')
ridhi_graph = transform_to_graph(ridhi)

solved_ridhi = solve_ridhi(ridhi, ridhi_graph, start_node, end_node)

print("\nSolved Maze:")
display_ridhi(ridhi)
