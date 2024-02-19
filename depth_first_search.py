from models.stack import Stack
from models.traversal_tree import Tree


class DFS():
    
    def __init__(self, graph) -> None:
        self.graph = graph
        self.stack = Stack()
        self.marked_vertices = {key: False for key in graph.keys()}
        self.traversal_tree = None
    
    def mark_visited(self, vertex):
        self.marked_vertices[vertex] = True

    def dfs(self, vertex):
        self.mark_visited(vertex)
        adjacent_vertices = self.graph[vertex]
        for adj_vertex in adjacent_vertices:
            if not self.marked_vertices[adj_vertex]:
                self.traversal_tree.add_child(adj_vertex)
                self.dfs(adj_vertex)

    def with_stack(self, s):
        self.stack.push(s)
        while not self.stack.is_empty():
            current_vertex = self.stack.peek()
            self.stack.pop()
            if not self.marked_vertices[current_vertex]:
                self.mark_visited(current_vertex)
                self.traversal_tree.add_child(current_vertex)
                adjacent_vertices = self.graph[current_vertex]
                for vertex in adjacent_vertices:
                    if not self.marked_vertices[vertex]:
                        self.stack.push(vertex)
       
    def complete_dfs(self, stack=False):
        forest = []
        for vertex in self.marked_vertices:
            if not self.marked_vertices[vertex]:
                self.traversal_tree = Tree(node=vertex)
                if stack:
                    self.with_stack(vertex)
                else:
                    self.dfs(vertex)
                forest.append(self.traversal_tree)
        return forest
    
