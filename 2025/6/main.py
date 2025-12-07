from functools import reduce
import functools
from types import new_class
from typing import Any, DefaultDict
from collections import defaultdict


def solution_one(data: str) -> Any:
    res = 0
    num_sets = defaultdict(list)
    op_sets = []
    for line in data.splitlines():
        i = 0
        for sym in line.split(" "):
            if sym == "":
                continue
            if sym == "*" or sym == "+":
                op_sets.append(sym)
                continue
            num_sets[i].append(int(sym))
            i += 1
    for i, op in enumerate(op_sets):
        if op == "+":
            res += sum(num_sets[i])
        else:
            res += reduce(lambda x, y: x * y, num_sets[i])
    return res


def solution_two(data: str) -> Any:
    res = 0
    lines = data.splitlines()
    grid: list[list[str]] = [list(x) for x in lines[:-1]]
    signs: list[str] = [x for x in lines[-1] if x.strip()]
    elements: list[list[int]] = [[]]
    for x in zip(*grid):
        if all([el == " " for el in x]):
            elements.append([])
            continue
        elements[-1].append(int("".join(x)))
    for els, sign in zip(elements, signs):
        if sign == "+":
            res += sum(els)
        else:
            res += functools.reduce(lambda x, y: x * y, els)
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
