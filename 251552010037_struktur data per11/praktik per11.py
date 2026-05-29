from tabnanny import check


class node:
    def __init__(self, value):
        self.data = value
        self.children = []
    
    def add_child(self, child_node) :
        self.children.append(child_node)

    def print_tree(self, level=0) :
        print("  " * level + f"- {self.value}")
        for child in self.children:
            child.print_tree(level + 1)

    def get_degree(self):
        return len(self.children)
    
    def get_height(self):
        if not self.children:
            return 1
        return 1 + max(child.get_height() for child in self.children)
    
root = node("A")
node_b = node("B")
node_c = node("C")
node_d = node("D")
node_e = node("E")
node_f = node("F")
node_g = node("G")

root.add_child(node_b)
root.add_child(node_c)

node_b.add_child(node_d)
node_b.add_child(node_e)

node_c.add_child(node_f)
node_f.add_child(node_g)

print("Tree Structure:")
root.print_tree()

print(f"\nDerajat node node A : {root.get_degree()}")
print(f"derajat node node B : {node_b.get_degree()}")
print(f"derajat node node f : {node_f.get_degree()}")
print(f"derajat node node g : {node_g.get_degree()}")

print(f"\ntinggi pohon dari root A: {root.get_height()}")


class binary_node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

root = binary_node("A")
root.left = binary_node("B")
root.right = binary_node("C")
root.left.left = binary_node("D")
root.left.right = binary_node("E")

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

print("binary tree - preorder traversal:")
preorder(root)

class node :
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_balanced(root):
    def check(node):
        if node is None:
            return 0, True
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        height = max(left_height, right_height) + 1
        balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1
        )
        return height, balanced
    _, balanced = check(root)
    return balanced

def print_tree(node, prefix="", is_left=True):
    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

root = node(10)
root.left = node(5)
root.right = node(15)
root.left.left = node(2)
root.left.right = node(7)
root.right.right = node(20)

print("visualisasi balanced tree:")
print_tree(root)

print("\napakah tree seimbang (balanced)?", is_balanced(root))

class bstnode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, new_key):
        if new_key < self.key:
            if self.left:
                self.left = self.left.insert(new_key)
            else:
                self.left = bstnode(new_key)
        elif new_key > self.key:
            if self.right:
                self.right = self.right.insert(new_key)
            else:
                self.right = bstnode(new_key)

    def inorder (self):
        if self.left:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right:
            self.right.inorder()

bst = bstnode(50)
for value in [30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("\nbinary search tree - inorder traversal;")
bst.inorder()

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = node("A")
root.left = node("B")
root.right = node("C")
root.left.left = node("D")
root.left.right = node("E")

def bfs_level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("BFS level order :")
bfs_level_order(root)

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = node("A")
root.left = node("B")
root.right = node("C")
root.left.left = node("D")
root.left.right = node("E")

def dfs_preorder(node):
    if node:
        print(node.value, end=' ')
        dfs_preorder(node.left)
        dfs_preorder(node.right)

def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=' ')
        dfs_inorder(node.right)

def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=' ')

print("DFS preorder :")
dfs_preorder(root)

print("\nDFS inorder :")
dfs_inorder(root)

print("\nDFS postorder :")
dfs_postorder(root)