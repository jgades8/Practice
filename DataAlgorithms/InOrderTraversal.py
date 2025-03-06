from BinaryTree import BinaryTree, Node


def in_order(root: Node):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    in_order(root)
