class Node:
    '''Node class for the red-black tree.'''
    def __init__(self, value, priority, color="RED"):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackPriorityQueue:
    '''A priority queue implemented using a red-black tree. Higher priority values are served first.'''
    def __init__(self):
        self.NIL = Node(None, None, color="BLACK")
        self.root = self.NIL

    def peek(self):
        '''Returns the value and priority of the highest priority item without removing it from the queue.'''
        if self.root == self.NIL:
            return None
        current = self.root
        while current.left != self.NIL:
            current = current.left
        return current.value, current.priority
    
    def insert(self, value, priority):
        '''Inserts a new item with the given value and priority into the queue.'''
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
        
        self._insert_fixup(new_node)

    def _insert_fixup(self, k):
        '''Fixes the tree after insertion to maintain red-black properties.'''
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def pop(self):
        ''''Removes and returns the value and priority of the highest priority item from the queue.'''
        if self.root == self.NIL:
            return None
            
        node_to_remove = self.root
        while node_to_remove.left != self.NIL:
            node_to_remove = node_to_remove.left
            
        result = (node_to_remove.value, node_to_remove.priority)
        self._delete_node(node_to_remove)
        return result


    def _delete_node(self, z):
        '''Deletes a node from the tree and fixes the tree to maintain red-black properties.'''
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = z.right
            while y.left != self.NIL:
                y = y.left
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == "BLACK":
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        '''Fixes the tree after deletion to maintain red-black properties.'''
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def _rb_transplant(self, u, v):
        '''Replaces the subtree rooted at node u with the subtree rooted at node v.'''
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _left_rotate(self, x):
        '''Performs a left rotation around the given node.'''
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        '''Performs a right rotation around the given node.'''
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x