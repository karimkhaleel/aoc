from typing import Any, NamedTuple
import heapq
import re
import z3


pattern = re.compile(
    r"(?P<machine_state>\[.*\]) (?P<buttons>(\((\d,?)+\)\s?)+)(?P<joltage>\{(\d,?)+\})"
)


class Node(NamedTuple):
    steps: int  # steps it took to get to this state
    dist: int  # distance to desired state
    state: tuple[bool, ...]  # current state


def get_dist(a: tuple[bool, ...], b: tuple[bool, ...]) -> int:
    return sum([x != y for x, y in zip(a, b)])


def find_shortest_path_state(
    final_state: tuple[bool, ...], buttons: list[list[int]]
) -> int:
    # Setup initial queue to search
    q: list[Node] = []
    seen_states: set[tuple[bool, ...]] = set()
    seen_states.add(tuple([False] * len(final_state)))

    for button in buttons:
        state = tuple((i in button) for i in range(len(final_state)))
        if state not in seen_states:
            dist = get_dist(state, final_state)
            if dist == 0:
                return 1
            seen_states.add(state)
            q.append(Node(1, dist, state))

    while q:
        steps, dist, state = heapq.heappop(q)
        for button in buttons:
            new_state_l = list(state)
            for b in button:
                new_state_l[b] = not new_state_l[b]
            new_state = tuple(new_state_l)

            if new_state in seen_states:
                continue
            seen_states.add(new_state)

            dist = get_dist(tuple(new_state), final_state)

            if dist == 0:
                return steps + 1

            heapq.heappush(q, Node(steps + 1, dist, new_state))

    return -1


def solution_one(data: str) -> Any:
    res = 0
    for line in data.splitlines():
        if match := re.match(pattern, line):
            final_state = tuple([s == "#" for s in match["machine_state"][1:-1]])
            buttons: list[list[int]] = []
            for button in match["buttons"].strip().split(" "):
                buttons.append([int(s) for s in button[1:-1].split(",")])
            res += find_shortest_path_state(final_state, buttons)
    return res


def solution_two(data: str) -> Any:
    res = 0
    for line in data.splitlines():
        if match := re.match(pattern, line):
            buttons: list[list[int]] = []
            final_joltage = [int(s) for s in match["joltage"][1:-1].split(",")]
            buttons_raw = match["buttons"].strip().split(" ")
            for button in buttons_raw:
                buttons.append([int(s) for s in button[1:-1].split(",")])
            button_presses = [z3.Int(f"x_{i}") for i in range(len(buttons))]
            s = z3.Optimize()
            for p in button_presses:
                s.add(p >= 0)
            for i in range(len(final_joltage)):
                increments_for_i = 0
                for j in range(len(buttons)):
                    if i in buttons[j]:
                        increments_for_i += button_presses[j]
                s.add(increments_for_i == final_joltage[i])
            total_presses = z3.Sum(button_presses)
            s.minimize(total_presses)
            if s.check() == z3.sat:
                model = s.model()
                res += sum(
                    [
                        model.evaluate(button_presses[i]).py_value()
                        for i in range(len(buttons))
                    ]
                )
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
