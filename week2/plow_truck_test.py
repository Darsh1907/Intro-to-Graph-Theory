import networkx as nx

grid = nx.MultiGraph(nx.grid_2d_graph(3,3))
grid = nx.eulerize(grid)
cycle = nx.eulerian_circuit(grid, (0, 0))
for edge in cycle:
    print(''.join(str(edge[0])))