from collections import defaultdict
import sys

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        coords = list(map(lambda s: [int(c) for c in s.strip()], f.readlines()))
        y_max = len(coords) - 1
        x_max = len(coords[0]) - 1

    distance_from_source = defaultdict(lambda: sys.maxsize)

    def traverse(
        current_position=(y_max, x_max),
        distance=0,
        visited=defaultdict(bool),
    ):
        distance += coords[current_position[0]][current_position[1]]
        visited[current_position[0], current_position[1]] = True
        if distance < distance_from_source[current_position]:
            distance_from_source[current_position] = distance
        else:
            return
        if current_position == (0, 0):
            return

        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            candidate_coords = (
                current_position[0] + move[0],
                current_position[1] + move[1],
            )
            if (
                0 <= candidate_coords[0] <= y_max
                and 0 <= candidate_coords[1] <= x_max
                and not visited[candidate_coords]
            ):
                try:
                    traverse(
                        candidate_coords,
                        distance,
                        visited.copy(),
                    )
                except IndexError:
                    pass

    visited = defaultdict(bool)
    visited[y_max, x_max] = True
    for move in ((0, -1), (-1, 0)):
        candidate_coords = (y_max + move[0], x_max + move[1])
        traverse(candidate_coords, distance=0, visited=visited)

    print(distance_from_source[0, 0])
