class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if item not in self.items:
            self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    
    def size(self):
        return len(self.items)
