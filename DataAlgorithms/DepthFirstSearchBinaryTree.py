from BinaryTree import BinaryTree, Node


def dfs_binary_tree(start: Node):
    if start:
        print(start.val)
        dfs_binary_tree(start.left)
        dfs_binary_tree(start.right)
