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
