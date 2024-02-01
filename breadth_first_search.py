from models.queue import Queue
from models.traversal_tree import Tree


class BFS:
    
    def __init__(self, graph):
        self.graph = graph
        self.queue = Queue()
        self.visited_vertices = {key: False for key in graph.keys()}
        self.traversal_tree = None

    def mark_visited(self, vertex):
        self.visited_vertices[vertex] = True
        self.queue.enqueue(vertex)

    def bfs(self, start_vertex):
        self.traversal_tree = Tree(node=start_vertex)
        self.mark_visited(start_vertex)
        
        while self.queue.size() != 0:
            current_vertex = self.queue.dequeue()
            self.traversal_tree.add_child(current_vertex)
            adjacent_vertices = self.graph[current_vertex] 
            for vertex in adjacent_vertices:
                if not self.visited_vertices[vertex]:
                    self.mark_visited(vertex)
        
    def complete_bfs(self): 
        forest = []
        for vertex in self.visited_vertices:
            if not self.visited_vertices[vertex]:
                self.bfs(start_vertex=vertex)
                forest.append(self.traversal_tree)  
        return forest
    
    def calculate_distance(self, source_vertex, destination_vertex):
        pass
