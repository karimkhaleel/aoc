from typing import Any


def solution_one(data: str) -> Any:
    pos = 50
    res = 0
    for line in data.splitlines():
        d, n = (
            line[0],
            int(line[1:]),
        )  # split into direction and number of clicks to rotate

        if d == "L":
            pos -= n
        else:
            pos += n

        if pos < 0 or pos > 99:
            pos %= 100

        if pos == 0:
            res += 1

    return res


def solution_two(data: str) -> Any:
    pos = 50
    res = 0
    for line in data.splitlines():
        d, n = (
            line[0],
            int(line[1:]),
        )  # split into direction and number of clicks to rotate

        zero_passes, n = divmod(n, 100)
        res += zero_passes

        # now check if we pass through/land on zero
        if d == "L":
            if pos != 0 and n >= pos:
                res += 1
            pos -= n
        else:
            if pos != 0 and n >= (100 - pos):
                res += 1
            pos += n

        if pos < 0 or pos > 99:
            pos %= 100

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
