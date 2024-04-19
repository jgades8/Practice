# Iterates through all values in a graph
# Uses QUEUE (NOT recursion)
# Searches closest to root first

def breadth_first_search(graph: dict, root: int):
    visited = set()
    queue = [root]
    visited.add(root)
    while queue:
        curr = queue.pop(0)
        print(f"visited {curr}")
        for i in graph[curr]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


if __name__ == '__main__':
    graph = {
        1: [2, 3, 5],
        2: [1, 4],
        3: [1, 5],
        4: [2],
        5: [1, 3]
    }
    breadth_first_search(graph, 1)
