class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.data = value

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
            else:
                binary_insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                binary_insert(root.right_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left_child)
    print(root.data)
    in_order_print(root.right_child)

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.left_child)
    pre_order_print(root.right_child)
