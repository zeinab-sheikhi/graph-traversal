from depth_first_search import DFS 
from utils.helper import sort_dict_keys, sort_dict_keys_by_list_order


def graph_transpose(graph):
    trans_graph = {key: [] for key in graph.keys()}
    for u in graph.keys():
        for v in graph[u]:
            trans_graph[v].append(u)

    return trans_graph


def scc(graph):
    dfs = DFS(graph)
    dfs.complete_dfs()
    ordering = sort_dict_keys(dfs.end_time)
    graph_t = graph_transpose(sort_dict_keys_by_list_order(graph, ordering))
    dfs_t = DFS(graph=graph_t)
    dfs_t.complete_dfs()
    return dfs_t.parent
