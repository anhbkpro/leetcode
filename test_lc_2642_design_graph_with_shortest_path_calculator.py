from lc_2642_design_graph_with_shortest_path_calculator import Graph
graph = Graph(n=4, edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])


def test_shortest_path():
    assert graph.shortestPath(node1=3, node2=2) == 6
    assert graph.shortestPath(node1=0, node2=3) == -1
    graph.addEdge(edge=[1, 3, 4])
    assert graph.shortestPath(node1=0, node2=3) == 6
