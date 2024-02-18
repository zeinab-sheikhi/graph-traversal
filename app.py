from depth_first_search import DFS

graph1 = {
    "A": ['B', 'D'],
    "B": ['A', 'C', 'E'],
    "C": ['B'],
    "D": ['A', 'E'],
    "E": ['B', 'D', 'F'],
    "F": ['E'],
}

dfs = DFS(graph=graph1)
forest = dfs.complete_dfs()
for tree in forest:
    print(tree)
