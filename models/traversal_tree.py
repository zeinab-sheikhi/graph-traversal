import networkx as nx
import matplotlib.pyplot as plt


class Tree:
    
    def __init__(self, node):
        self.root = node
        self.children = []
    
    def add_child(self, child):
        if child != self.root:
            self.children.append(child)

    def __str__(self) -> str:
        tree_str = "Root is: " + self.root + "\n" + "Children are: \n"
        for child in self.children:
            tree_str += child + " "
        return tree_str


def print_tree(node, level=0):
    if node is None:
        return

    print("    " * level + str(node.data))
    for child in node.children:
        print_tree(child, level + 1)


def draw_tree(parent_dict):
    G = nx.DiGraph()
    
    for child, parent in parent_dict.items():
        G.add_edge(parent, child)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.show()

