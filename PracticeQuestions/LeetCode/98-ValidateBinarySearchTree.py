from BinaryTree import Node


def validate_bst(root: Node):

    order = []

    def in_order(root: Node):
        if root:
            in_order(root.left)
            order.append(root.val)
            in_order(root.right)

    in_order(root)
    print(order)
    if order == sorted(order):
        return True
    else:
        return False


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    root2 = Node(6)
    root2.left = Node(4)
    root2.right = Node(7)
    root2.left.left = Node(3)
    root2.left.right = Node(5)
    root2.right.right = Node(8)

    print(validate_bst(root))
    print(validate_bst(root2))

