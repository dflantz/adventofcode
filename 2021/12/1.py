from collections import defaultdict
from typing import Dict, List


def find_paths(
    state: str,
    graph: Dict[str, List[str]],
    all_paths: List[List[str]],
    current_path: List[str] = [],
):
    current_path.append(state)
    routes = graph[state]
    for r in routes:
        if r == "end":
            current_path.append(r)
            all_paths.append(current_path)
        else:
            if (r.islower() and r not in current_path) or r.isupper():
                find_paths(r, graph, all_paths, current_path.copy())


if __name__ == "__main__":
    cave_graph = defaultdict(list)
    for line in open("2021/12/input.txt", "r"):
        a, b = line.strip().split("-")
        cave_graph[a].append(b)
        cave_graph[b].append(a)

    all_paths = []
    find_paths("start", cave_graph, all_paths, [])
    print(len(all_paths))
