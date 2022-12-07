import sys

if __name__ == "__main__":
    with open("15/input.txt", "r") as f:
        coords = list(map(lambda s: [int(c) for c in s.strip()], f.readlines()))
        y_max = len(coords)
        x_max = len(coords[0])

    visited = [[False for _ in range(x_max)] for _ in range(y_max)]
    distance_from_source = [[sys.maxsize for _ in range(x_max)] for _ in range(y_max)]

    visited[0][0] = True

    def traverse(current_position=(0, 0), distance=0):
        visited[current_position[0]][current_position[1]] = True

        if current_position == (y_max, x_max):
            return
        unvisited_neighbors = []

        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y, x = current_position[0] + move[0], current_position[1] + move[1]
            if 0 <= y < y_max and 0 <= x < x_max and not visited[y][x]:
                curr_distance = distance + coords[y][x]
                distance_from_source[y][x] = min(
                    curr_distance, distance_from_source[y][x]
                )
                unvisited_neighbors.append(((y, x), distance_from_source[y][x]))

        if unvisited_neighbors:
            neighbor = sorted(unvisited_neighbors, key=lambda x: x[1])[0]
            traverse(neighbor[0], neighbor[1])
        else:
            print("all neighbors visited for {current_position}")

    traverse()

    # print(visited)
    for l in distance_from_source:
        print(l)
