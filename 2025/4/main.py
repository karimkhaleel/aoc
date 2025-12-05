from typing import Any

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solution_one(data: str) -> Any:
    res = 0
    d = data.splitlines()
    for y in range(len(d)):
        for x in range(len(d[y])):
            if d[y][x] != "@":
                continue

            num_rolls = 0
            for dy, dx in dirs:
                ny, nx = (y + dy), (x + dx)
                if 0 <= ny < len(d) and 0 <= nx < len(d[y]) and d[ny][nx] == "@":
                    num_rolls += 1

            if num_rolls < 4:
                res += 1
    return res


def solution_two(data: str) -> Any:
    res = 0
    d = [list(x) for x in data.splitlines()]
    have_removed = True
    while have_removed:
        have_removed = False

        for y in range(len(d)):
            for x in range(len(d[y])):
                if d[y][x] != "@":
                    continue

                num_rolls = 0
                for dy, dx in dirs:
                    ny, nx = (y + dy), (x + dx)
                    if 0 <= ny < len(d) and 0 <= nx < len(d[y]) and d[ny][nx] == "@":
                        num_rolls += 1

                if num_rolls < 4:
                    res += 1
                    have_removed = True
                    d[y][x] = "."
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
