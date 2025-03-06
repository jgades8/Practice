
def find_lca(tree: [], p: int, q: int, current_node):
    node = tree[current_node] # root node
    if (p < node < q) or (p > node > q):
        return node
    elif node == q:
        return q
    elif node == p:
        return p
    elif p < node and q < node:
        # move to left node
        current_node += 1
        return find_lca(tree, p, q, current_node)
    elif p > node and q > node:
        # move to right node
        current_node += 2
        return find_lca(tree, p, q, current_node)


if __name__ == '__main__':
    tree = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 3
    q = 5
    print(find_lca(tree, p, q, 0))
