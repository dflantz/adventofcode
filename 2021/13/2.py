from collections import defaultdict
from typing import Dict, List


def find_paths(
    state: str,
    graph: Dict[str, List[str]],
    all_paths: List[List[str]],
    current_path: List[str] = [],
    small_cave_visited_twice: bool = False,
):
    current_path.append(state)
    routes = graph[state]
    for r in routes:
        if r == "end":
            current_path.append(r)
            all_paths.append(current_path)
        elif r == "start":
            continue
        else:
            if r.islower():
                occurrences = current_path.count(r)
                if occurrences == 0:
                    find_paths(
                        r,
                        graph,
                        all_paths,
                        current_path.copy(),
                        small_cave_visited_twice=small_cave_visited_twice,
                    )
                elif occurrences == 1 and not small_cave_visited_twice:
                    find_paths(
                        r,
                        graph,
                        all_paths,
                        current_path.copy(),
                        small_cave_visited_twice=True,
                    )
            else:
                find_paths(
                    r,
                    graph,
                    all_paths,
                    current_path.copy(),
                    small_cave_visited_twice=small_cave_visited_twice,
                )


if __name__ == "__main__":
    cave_graph = defaultdict(list)
    for line in open("2021/12/input.txt", "r"):
        a, b = line.strip().split("-")
        cave_graph[a].append(b)
        cave_graph[b].append(a)

    all_paths = []
    find_paths("start", cave_graph, all_paths, [])
    # print(all_paths)
    print(len(all_paths))
