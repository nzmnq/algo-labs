import os


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    @staticmethod
    def deserialize_postorder(data: str):
        if not data:
            return None
        tokens = data.strip().split()

        def build():
            if not tokens:
                return None
            val = tokens.pop()
            if val == "nil":
                return None
            node = BinaryTree(int(val))
            node.right = build()
            if node.right:
                node.right.parent = node
            node.left = build()
            if node.left:
                node.left.parent = node
            return node

        return build()

    def print_tree(self):
        def get_h(node):
            if not node: return 0
            return max(get_h(node.left), get_h(node.right)) + 1
        
        h = get_h(self)
        if h == 0: return
        
        col_width = 1 
        width = (2**h) * col_width
        matrix = [[" " for _ in range(width)] for _ in range(h * 2)]
        
        def place(r, c, txt):
            s = str(txt)
            start_c = c - len(s) // 2
            for i, char in enumerate(s):
                if 0 <= start_c + i < width:
                    matrix[r][start_c + i] = char

        def fill(node, depth, left_bound, right_bound):
            if not node:
                return
            
            mid = (left_bound + right_bound) // 2
            val_str = str(node.value)
            place(depth * 2, mid, val_str)

            left_offset = 1 if len(val_str) % 2 == 0 else 0
            
            if node.left:
                child_mid = (left_bound + mid) // 2
                slash_pos = (mid + child_mid) // 2 - left_offset
                place(depth * 2 + 1, slash_pos, "/")
                fill(node.left, depth + 1, left_bound, mid)
                
            if node.right:
                child_mid = (mid + right_bound) // 2
                slash_pos = (mid + child_mid) // 2
                place(depth * 2 + 1, slash_pos, "\\")
                fill(node.right, depth + 1, mid, right_bound)

        fill(self, 0, 0, width)
        
        for row in matrix:
            line = "".join(row).rstrip()
            if line:
                print(line)
if __name__ == "__main__":
    filename = "pre_tree.txt"
    if not os.path.exists(filename):
        print(f"file {filename} not found")
        exit(1)

    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read().strip()

    print(f"data from: {file_content}\n")
    root = BinaryTree.deserialize_postorder(file_content)

    if root:
        root.print_tree()
    else:
        print("tree is empty")