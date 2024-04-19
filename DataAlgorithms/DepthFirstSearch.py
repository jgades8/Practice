# Iterates through all values in a graph
# Explores entire branch completely before moving to next node

def depth_first_search(visited: set, graph: dict, node: int):
    if node not in visited:
        print(f"visited {node}")
        visited.add(node)
        for neighbor in graph[node]:
            depth_first_search(visited, graph, neighbor)


if __name__ == '__main__':
    graph = {
        1: [2, 3, 5],
        2: [1, 4],
        3: [1, 5],
        4: [2],
        5: [1, 3]
    }
    visited = set()

    depth_first_search(visited, graph, 1)
