from BinaryTree import BinaryTree, Node


def post_order(root: Node):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    post_order(root)
