from models.stack import Stack
from models.traversal_tree import Tree


class DFS():
    
    def __init__(self, graph) -> None:
        self.graph = graph
        self.stack = Stack()
        self.marked_vertices = {key: False for key in graph.keys()}
        self.traversal_tree = None
        self.forest = []
        self.topological_sorting = []
    
    def mark_as_visited(self, vertex):
        self.marked_vertices[vertex] = True
    
    def recursive_dfs(self, vertex):
        self.mark_as_visited(vertex)
        adjacent_vertices = self.graph[vertex]
        for adj_vertex in adjacent_vertices:
            if not self.marked_vertices[adj_vertex]:
                self.traversal_tree.add_child(adj_vertex)
                self.recursive_dfs(adj_vertex)
        self.topological_sorting.append(vertex)

    def dfs_with_stack(self, s):
        self.stack.push(s)
        while not self.stack.is_empty():
            current_vertex = self.stack.peek()
            self.stack.pop()
            if not self.marked_vertices[current_vertex]:
                self.mark_as_visited(current_vertex)
                self.traversal_tree.add_child(current_vertex)
                adjacent_vertices = self.graph[current_vertex]
                for vertex in adjacent_vertices:
                    if not self.marked_vertices[vertex]:
                        self.stack.push(vertex)          
       
    def complete_dfs(self, stack=False):
        for vertex in self.marked_vertices:
            if not self.marked_vertices[vertex]:
                self.traversal_tree = Tree(node=vertex)
                if stack:
                    self.dfs_with_stack(vertex)
                else:
                    self.recursive_dfs(vertex)
                self.forest.append(self.traversal_tree)
        self.topological_sorting.reverse()
    