from typing import Any


def solution_one(data: str) -> Any:
    res = 0
    grid = data.splitlines()
    beams: list[bool] = [x == "S" for x in grid[0]]
    for line in grid[1:]:
        new_beams = beams[::]
        for i, (x, beam_on) in enumerate(zip(line, beams)):
            if x == "^":
                new_beams[i] = False  # beam gets split
                if beam_on:
                    res += 1
                    if i > 0:
                        new_beams[i - 1] = True
                    if i < len(beams) - 1:
                        new_beams[i + 1] = True
        beams = new_beams
    return res


def solution_two(data: str) -> Any:
    grid = data.splitlines()
    beams: list[int] = [1 if x == "S" else 0 for x in grid[0]]
    for line in grid[1:]:
        new_beams = beams[::]
        for i, (x, beam_on) in enumerate(zip(line, beams)):
            if x == "^":
                new_beams[i] = 0
                if beam_on:
                    if i > 0:
                        new_beams[i - 1] += beams[i]
                    if i < len(beams) - 1:
                        new_beams[i + 1] += beams[i]
        beams = new_beams
    return sum(beams)


def main():
    with open("input.txt", "r") as f:
        data = f.read()
        print(f"one -> {solution_one(data)}")
        print(f"two -> {solution_two(data)}")


if __name__ == "__main__":
    main()


def test_solution() -> None:
    pass
