from typing import Any


def solution_one(data: str) -> Any:
    res = 0
    for line in data.splitlines():
        digits = [int(i) for i in line]
        li = 0

        for i in range(len(digits) - 1):
            if digits[i] > digits[li]:
                li = i

        ri = li + 1
        for i in range(li + 1, len(digits)):
            if digits[i] > digits[ri]:
                ri = i

        ld = digits[li]
        rd = digits[ri]
        joltage = int(f"{ld}{rd}")
        res += joltage
    return res


def find_largest(digits: list[int], start: int, end: int) -> int:
    li = start
    for i in range(start, end + 1):
        if digits[i] > digits[li]:
            li = i
    return li


def solution_two(data: str) -> Any:
    res = 0
    for line in data.splitlines():
        digits = [int(i) for i in line]
        chosen_digits = []
        li = 0
        for i in reversed(range(1, 13)):
            li = find_largest(digits, li, len(digits) - i)
            chosen_digits.append(str(digits[li]))
            li += 1

        joltage = int("".join(chosen_digits))
        res += joltage

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
