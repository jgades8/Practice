from BinaryTree import Node


def bfs_binary_tree(root: Node):
    queue = [root]

    while queue:
        curr = queue.pop(0)
        print(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    bfs_binary_tree(root)
