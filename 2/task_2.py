def my_code(adjacency_graph_nodes: dict, initial_vertex: int, visited_peaks: list = []):

    if not visited_peaks:
        visited_peaks = []

    if initial_vertex not in visited_peaks:
        visited_peaks.append(initial_vertex)
        print(initial_vertex)

    adjacency_graph_nodes[initial_vertex] = [adjacency_graph_nodes[initial_vertex]] if type(adjacency_graph_nodes[initial_vertex]) == int else adjacency_graph_nodes[initial_vertex]

    for adjacent_vertex in adjacency_graph_nodes[initial_vertex]:
        if adjacent_vertex in adjacency_graph_nodes.keys():
            del adjacency_graph_nodes[initial_vertex]
            my_code(
                adjacency_graph_nodes=adjacency_graph_nodes, 
                initial_vertex=int(adjacent_vertex),
                visited_peaks=visited_peaks 
            )
        else:
            if adjacent_vertex not in visited_peaks:
                visited_peaks.append(adjacent_vertex)
                print(adjacent_vertex)


print("\nCASE 1\n")
data = {
    1: [2, 3],
    2: [4]
}

my_code(data, 1)


print("\nCASE 2\n")
data = {
    1: [2, 3],
    2: [3, 4],
    4: 1
}
my_code(data, 1)