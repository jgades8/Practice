# Given a directed graph and 2 nodes (S and E),
# design an algorithm to determine if there is a route from S to E

def path_between(visited: set, graph: dict, start: str, end: str):
    if start in graph and end in graph:   # No need to check this every time
        if start not in visited:
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:   # This is necessary if graph can be multi-directional
                    if neighbor == end:
                        return True
                    else:
                        path_exists = path_between(visited, graph, neighbor, end)
                        if path_exists:
                            return True
    return False


if __name__ == '__main__':
    start = "S"
    end = "E"

    graph_true = {
        "S": ["L", "Q", "A"],
        "A": ["E"],
        "Q": ["S", "L"],
        "L": [],
        "E": []
    }

    graph_false = {
        "A": ["B", "S"],
        "B": ["E"],
        "S": ["C", "Z"],
        "C": [],
        "Z": [],
        "E": []

    }

    print(path_between(set(), graph_true, "S", "E"))
    print(path_between(set(), graph_false, "S", "E"))
