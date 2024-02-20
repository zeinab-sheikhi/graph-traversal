from depth_first_search import DFS
from models.traversal_tree import draw_tree, print_tree


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

dfs = DFS(graph=graph1)
dfs.complete_dfs(stack=False)
print(dfs.parent)
print(dfs.start_time)
print(dfs.end_time)
print(dfs.traversed_edges)
print(dfs.edge_type)
if not dfs.is_acyclic():
    print(dfs.topological_sorting)
