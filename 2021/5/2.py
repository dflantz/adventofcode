from typing import Dict, List, NamedTuple, Optional, Set, Tuple


class Point(NamedTuple):
    x: int
    y: int


class Vent(NamedTuple):
    p1: Point
    p2: Point


def get_interceding_points(vent: Vent) -> List[Point]:
    y_min, y_max = min(vent.p1.y, vent.p2.y), max(vent.p1.y, vent.p2.y)
    x_min, x_max = min(vent.p1.x, vent.p2.x), max(vent.p1.x, vent.p2.x)
    if vent.p1.x == vent.p2.x:
        return [Point(vent.p1.x, y) for y in range(y_min, y_max + 1)]
    elif vent.p1.y == vent.p2.y:
        return [Point(x, vent.p2.y) for x in range(x_min, x_max + 1)]
    else:
        slope = (vent.p2.y - vent.p1.y) / (vent.p2.x - vent.p1.x)
        if slope > 0:
            return [
                Point(x, y)
                for x, y in zip(range(x_min, x_max + 1), range(y_min, y_max + 1))
            ]
        else:
            return [
                Point(x, y)
                for x, y in zip(range(x_min, x_max + 1), range(y_max, y_min - 1, -1))
            ]


if __name__ == "__main__":
    vents: List[Vent] = []

    grid: Dict[Point, int] = {}

    for line in open("2021/5/input.txt"):
        p1, p2 = line.split("->")
        x1, y1 = p1.strip().split(",")
        x2, y2 = p2.strip().split(",")

        # if x1 == x2 or y1 == y2:
        vents.append(
            Vent(p1=Point(x=int(x1), y=int(y1)), p2=Point(x=int(x2), y=int(y2)))
        )

    points_with_2_vents: Set[Point] = set()
    for vent in vents:
        for point in get_interceding_points(vent):
            if point in grid:
                grid[point] += 1
                if grid[point] >= 2:
                    points_with_2_vents.add(point)
            else:
                grid[point] = 1

    print(len(points_with_2_vents))
