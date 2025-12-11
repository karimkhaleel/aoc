import functools
from typing import Any


adj: dict[str, list[str]] = {}


def get_adj(data: str) -> dict[str, list[str]]:
    adj: dict[str, list[str]] = {}
    for line in data.splitlines():
        device, outs_raw = line.split(":")
        outs = outs_raw.strip().split(" ")
        adj[device] = outs
    adj["out"] = []
    return adj


@functools.cache
def dfs(a: str, b: str) -> int:
    if a == b:
        return 1

    global adj

    return sum(dfs(next_node, b) for next_node in adj[a])


def solution_one(data: str) -> Any:
    return dfs("you", "out")


def solution_two(data: str) -> Any:
    svr_dac = dfs("svr", "dac")
    dac_fft = dfs("dac", "fft")
    fft_out = dfs("fft", "out")

    svr_fft = dfs("svr", "fft")
    fft_dac = dfs("fft", "dac")
    dac_out = dfs("dac", "out")

    return (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)


def main():
    with open("input.txt", "r") as f:
        data = f.read()

        global adj
        adj = get_adj(data)

        print(f"one -> {solution_one(data)}")
        print(f"two -> {solution_two(data)}")


if __name__ == "__main__":
    main()


def test_solution() -> None:
    pass

