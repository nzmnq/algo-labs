class Node:
    def __init__(self, value, priority, color="RED"):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, None, color="BLACK")
        self.root = self.NIL

    def peek(self):
        if self.root == self.NIL:
            return None
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current.value, current.priority
    
    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None 
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.priority >= current.priority:
                current = current.left
            else:
                current = current.right

            new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.priority >= parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node. color = "BLACK"
            return
        
        if new_node.parent.parent is None:
            return
        
        self.fix_insert(new_node)

        ''' developing....'''