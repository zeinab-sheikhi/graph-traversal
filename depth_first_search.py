from models.stack import Stack


class DFS():
    
    def __init__(self, graph) -> None:
        self.graph = graph
        self.stack = Stack()
        self.visited_vertices = {key: False for key in graph.keys()}
        self.parent = {key: None for key in graph.keys()}
        self.edges = [(key, value) for key, values in graph.items() for value in values]
        self.edge_type = {}
        self.traversed_edges = []
        self.start_time = {}
        self.end_time = {}
        self.topological_sorting = []
        self.time = 0
    
    def complete_dfs(self, stack=False):
        for vertex in self.visited_vertices:
            if not self.visited(vertex):
                if stack:
                    self.dfs_with_stack(vertex)
                else:
                    self.recursive_dfs(vertex)
        self.topological_sorting.reverse()
        self.set_edge_type()

    def recursive_dfs(self, vertex):
        self.set_visited(vertex)
        self.set_start_time(vertex)
        adjacent_vertices = self.graph[vertex]
        for adj_vertex in adjacent_vertices:
            if not self.visited(adj_vertex):
                self.parent[adj_vertex] = vertex
                self.traversed_edges.append((vertex, adj_vertex))
                self.recursive_dfs(adj_vertex)
        self.set_end_time(vertex)
        self.topological_sorting.append(vertex)

    def set_visited(self, vertex):
        self.visited_vertices[vertex] = True
    
    def set_start_time(self, vertex):
        self.start_time[vertex] = self.time
        self.time += 1
    
    def set_end_time(self, vertex):
        self.end_time[vertex] = self.time
        self.time += 1

    def set_edge_type(self):
        for edge in self.edges:
            if edge not in self.traversed_edges:
                node, neighbor = edge
                if self.start_time[node] > self.start_time[neighbor] and self.end_time[node] < self.end_time[neighbor]:
                    self.edge_type[(node, neighbor)] = "backward"
                elif self.start_time[node] < self.start_time[neighbor] and self.end_time[node] > self.end_time[neighbor]:
                    self.edge_type[(node, neighbor)] = "forward"
                elif self.start_time[node] > self.start_time[neighbor] and self.end_time[node] > self.end_time[neighbor]:
                    self.edge_type[(node, neighbor)] = "transversed"

    def visited(self, vertex):
        if self.visited_vertices[vertex]:
            return True
        return False    
    
    def is_acyclic(self):
        for types in self.edge_type.values():
            if "backward" not in types:
                return True
        return False
    
    def dfs_with_stack(self, s):
        self.stack.push(s)
        while not self.stack.is_empty():
            current_vertex = self.stack.peek()
            self.stack.pop()
            if not self.visited(current_vertex):
                self.set_visited(current_vertex)
                self.set_start_time(current_vertex)
                adjacent_vertices = self.graph[current_vertex]
                for vertex in adjacent_vertices:
                    if not self.visited(vertex):
                        self.parent[vertex] = current_vertex
                        self.stack.push(vertex) 
                self.set_end_time(current_vertex)         
       
