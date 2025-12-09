from typing import Any, Iterable, NamedTuple, Sequence


class Coords(NamedTuple):
    x: int
    y: int


def get_area(a: Coords, b: Coords) -> int:
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def solution_one(data: str) -> Any:
    res = 0
    coords = []

    for li in data.splitlines():
        coords.append(Coords(*(int(x) for x in li.split(","))))
    for i in range(len(coords)):
        a = coords[i]
        for j in range(i + 1, len(coords)):
            b = coords[j]
            res = max(res, get_area(a, b))
    return res


def line(p: Coords, q: Coords) -> set[Coords]:
    li = set()
    a1, a2 = min(p.x, q.x), max(p.x, q.x)
    b1, b2 = min(p.y, q.y), max(p.y, q.y)
    for a in range(a1, a2 + 1):
        for b in range(b1, b2 + 1):
            li.add(Coords(a, b))
    return li


def perimeter(c: Sequence[Coords]) -> set[Coords]:
    p = set()
    for i in range(1, len(c)):
        p |= line(c[i - 1], c[i])
    return p | line(c[-1], c[0])


def is_contained_by_perimeter(p: Coords, q: Coords, perimeter: set[Coords]) -> bool:
    a1, a2 = min(p.x, q.x), max(p.x, q.x)
    b1, b2 = min(p.y, q.y), max(p.y, q.y)
    for a, b in perimeter:
        if a1 < a < a2 and b1 < b < b2:
            return False
    return True


def solution_two(data: str) -> Any:
    coords: list[Coords] = []
    for line in data.splitlines():
        coords.append(Coords(*(int(x) for x in line.split(","))))

    areas: list[tuple[Coords, Coords, int]] = []
    for i in range(len(coords)):
        a = coords[i]
        for j in range(i + 1, len(coords)):
            b = coords[j]
            areas.append((a, b, get_area(a, b)))

    areas.sort(key=lambda x: x[2], reverse=True)
    perimeters = perimeter(coords)
    for a, b, area in areas:
        if is_contained_by_perimeter(a, b, perimeters):
            return area
    return 0


def main():
    with open("input.txt", "r") as f:
        data = f.read()
        print(f"one -> {solution_one(data)}")
        print(f"two -> {solution_two(data)}")


if __name__ == "__main__":
    main()


def test_solution() -> None:
    pass
