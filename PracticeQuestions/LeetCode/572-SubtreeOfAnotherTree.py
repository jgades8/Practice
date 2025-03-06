# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # breadth first search, first find root of subtree
    queue = [root]
    subQueue = [subRoot]
    while queue:
        s = queue.pop(0)
        if s.val == subRoot.val:
            # found the sub root node in main tree
            queue1 = [s]
            sr = subRoot
            while subQueue:
                if s.left is not None:
                    queue1.append(s.left)
                else:
                    # check if sr also None
                    if sr.left is not None:
                        return False
                subQueue.append(sr.left)
                queue1.append(s.right)
                subQueue.append(sr.right)
                if queue1.pop(0).val != subQueue.pop(0).val:
                    return False
            return True
        queue.append(s.left)
        queue.append(s.right)

    # TODO: first find all potential root nodes that match root of sub tree
    if root and subRoot:

    # TODO: secondary fn to compare if 2 trees are identical


if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(5)
    root.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.left = TreeNode(1)

    subroot = TreeNode(4)
    subroot.right = TreeNode(2)
    subroot.left = TreeNode(1)

    print(isSubtree(root, subroot))
