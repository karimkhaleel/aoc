from typing import Any
import re


def solution_one(data: str) -> Any:
    res = 0
    for r in data.split(","):
        start, end = (int(x) for x in r.split("-"))
        for i in range(start, end + 1):
            si = str(i)
            if si[: len(si) // 2] == si[len(si) // 2 :]:
                res += i
    return res


def solution_two(data: str) -> Any:
    res = 0
    for r in data.split(","):
        start, end = (int(x) for x in r.split("-"))
        for i in range(start, end + 1):
            si = str(i)
            m = re.match(r"(?P<p>\d+)(?:(?P=p))+$", si)
            if m is not None:
                res += i

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
