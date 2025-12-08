from collections import defaultdict
from typing import Any, NamedTuple
from math import prod, sqrt


class Coords(NamedTuple):
    x: int
    y: int
    z: int


class CoordPair(NamedTuple):
    a: Coords
    b: Coords


def dist(a: Coords, b: Coords) -> float:
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


def find(circuits: dict[Coords, Coords], c: Coords) -> Coords:
    if circuits[c] != c:
        circuits[c] = find(circuits, circuits[c])
    return circuits[c]


def union(circuits: dict[Coords, Coords], a: Coords, b: Coords) -> bool:
    root_a = find(circuits, a)
    root_b = find(circuits, b)
    if root_a != root_b:
        circuits[root_b] = root_a
        return True
    return False


def solution_one(data: str) -> Any:
    coords = []
    for line in data.splitlines():
        coords.append(Coords(*(int(x) for x in line.split(","))))

    dists: list[tuple[float, CoordPair]] = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dists.append(
                (dist(coords[i], coords[j]), CoordPair(*sorted([coords[i], coords[j]])))
            )

    dists.sort()

    circuits: dict[Coords, Coords] = {c: c for c in coords}
    for _, (a, b) in dists[:1000]:
        union(circuits, a, b)

    counts = defaultdict(int)
    for c in circuits:
        counts[find(circuits, c)] += 1
    return prod(sorted(counts.values(), reverse=True)[:3])


def solution_two(data: str) -> Any:
    coords = []
    for line in data.splitlines():
        coords.append(Coords(*(int(x) for x in line.split(","))))

    dists: list[tuple[float, CoordPair]] = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dists.append(
                (dist(coords[i], coords[j]), CoordPair(*sorted([coords[i], coords[j]])))
            )

    dists.sort()

    circuits: dict[Coords, Coords] = {c: c for c in coords}
    num_circuits = len(coords)
    for i, (_, pair) in enumerate(dists):
        a, b = pair
        if union(circuits, a, b):
            num_circuits -= 1
        if num_circuits == 1:
            return a.x * b.x
    return -1


def main():
    with open("input.txt", "r") as f:
        data = f.read()
        print(f"one -> {solution_one(data)}")
        print(f"two -> {solution_two(data)}")


if __name__ == "__main__":
    main()


def test_solution() -> None:
    pass

