from typing import Any, NamedTuple

type IngredientIDs = list[int]
type Ranges = list[Range]


class Range(NamedTuple):
    start: int
    end: int

    def __contains__(self, key: object, /) -> bool:
        if isinstance(key, int):
            return self.start <= key <= self.end

        return False


def parse(data: str) -> tuple[Ranges, IngredientIDs]:
    ranges: list[Range] = []
    ids: IngredientIDs = []
    in_ranges = True
    for line in data.splitlines():
        if line == "":
            in_ranges = False
            continue

        if in_ranges:
            start, end = line.split("-")
            ranges.append(Range(int(start), int(end)))
        else:
            ids.append(int(line))
    return ranges, ids


def solution_one(data: str) -> Any:
    res = 0
    ranges, ids = parse(data)
    ranges.sort()
    sranges = [ranges[0]]
    for r in ranges[1:]:
        if sranges[-1].end >= r.start:
            sranges[-1] = Range(sranges[-1].start, max(sranges[-1].end, r.end))
        else:
            sranges.append(r)

    for i in ids:
        for r in ranges:
            if i in r:
                res += 1
                break
    return res


def solution_two(data: str) -> Any:
    res = 0
    ranges, ids = parse(data)
    ranges.sort()
    sranges = [ranges[0]]
    for r in ranges[1:]:
        if sranges[-1].end >= r.start:
            sranges[-1] = Range(sranges[-1].start, max(sranges[-1].end, r.end))
        else:
            sranges.append(r)

    for r in sranges:
        res += r.end - r.start + 1

    return res


def main():
    with open("input.txt", "r") as f:
        data = f.read()
        print(f"one -> {solution_one(data)}")
        print(f"two -> {solution_two(data)}")


if __name__ == "__main__":
    main()


def test_solution() -> None:
    pass
