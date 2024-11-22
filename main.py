from graph import Graph
from ford_fulkerson import FordFulkerson

graph = Graph()
graph.add_nodes(['S', 'A', 'C', 'B', 'D', 'T'])
graph.add_edge('S', 'A', 4)
graph.add_edge('S', 'C', 3)
graph.add_edge('A', 'B', 4)
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'T', 2)
graph.add_edge('C', 'D', 6)
graph.add_edge('D', 'T', 6)

starting_node = 'S'
ending_node = 'T'
method = FordFulkerson(graph, starting_node, ending_node)

print(f"The maximum possible flow is {method.initiate()}")