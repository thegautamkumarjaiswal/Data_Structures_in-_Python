# Implementation of In-order, Pre-order, Post-order in Binary Search Tree#
class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):    # define the Insertion #
    if root is None:
        return Tree(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# In-order Traversal#
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

# Pre-order Traversal#
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

# Post-order Traversal#
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

# main function #
r = Tree(60)
r = insert(r, 70)
r = insert(r, 30)
r = insert(r, 80)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 10)
r = insert(r, 20)
print("In Order:")
in_order(r)

print("\nPre Order:")
pre_order(r)

print("\nPost Order:")
post_order(r)

