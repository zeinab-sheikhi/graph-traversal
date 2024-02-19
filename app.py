from depth_first_search import DFS

graph1 = {
    "A": ['B', 'D'],
    "B": ['A', 'C', 'E'],
    "C": ['B'],
    "D": ['A', 'E'],
    "E": ['B', 'D', 'F'],
    "F": ['E'],
}

graph2 = {
    "0": ["1", "2"],
    "1": ["0", "3"],
    "2": ["0", "1", "3"],
    "3": ["1", "2"],
    "4": ["5", "6"],
    "5": ["4", "6"],
    "6": ["4", "5", "7"],
    "7": ["6"],
}

dfs = DFS(graph=graph2)
forest = dfs.complete_dfs(stack=True)
for tree in forest:
    print(tree)
