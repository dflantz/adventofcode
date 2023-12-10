from collections import defaultdict
from heapq import heappop, heappush
import sys

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        coords = list(map(lambda s: [int(c) for c in s.strip()], f.readlines()))
        tile_height = len(coords)
        tile_width = len(coords[0])
        num_tiles = 5
        y_max = tile_height * num_tiles - 1
        x_max = tile_width * num_tiles - 1

    distance_from_source = defaultdict(lambda: sys.maxsize)

    positions_to_evaluate = [(0, 0, 0)]
    visited = defaultdict(bool)

    while len(positions_to_evaluate):
        distance, y, x = heappop(positions_to_evaluate)
        if visited[y, x]:
            continue
        visited[y, x] = True

        # check neighbors.
        for y_move, x_move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            candidate_y, candidate_x = (y + y_move, x + x_move)
            if 0 <= candidate_y <= y_max and 0 <= candidate_x <= x_max:
                weight = coords[candidate_y % tile_height][candidate_x % tile_width]
                weight += candidate_y // tile_height
                weight += candidate_x // tile_width
                if weight % 9 == 0:
                    weight = 9
                else:
                    weight %= 9
                distance_from_source[candidate_y, candidate_x] = min(
                    distance_from_source[candidate_y, candidate_x], distance + weight
                )
                heappush(
                    positions_to_evaluate,
                    (
                        distance_from_source[candidate_y, candidate_x],
                        candidate_y,
                        candidate_x,
                    ),
                )

    print(distance_from_source[x_max, y_max])
