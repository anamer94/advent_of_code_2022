from functools import reduce
from typing import List

with open("day5.txt", "r") as f:
    lines = f.readlines()

initial_state_str = lines[:lines.index("\n")]
instructions = lines[lines.index("\n") + 1:]


def parse_initial_state(lines: List[str]) -> List[List[str]]:
    n_queues = int(lines[-1].strip().split("   ")[-1])

    stacks = []
    for i in range(n_queues):
        stacks.append([])

    for i in range(len(lines) - 2, -1, -1):
        for j in range(n_queues):
            if 1 + 4 * j >= len(lines[i]):
                continue
            crate = lines[i][1 + 4 * j]
            if crate != " ":
                stacks[j].append(crate)
    return stacks


def apply_instruction(state: List[List[str]], instruction: str) -> List[List[str]]:
    split_instruction = instruction.split()
    quantity = int(split_instruction[1])
    from_stack = int(split_instruction[3]) - 1
    to_stack = int(split_instruction[5]) - 1
    for i in range(quantity):
        if len(state[from_stack]) == 0:
            break
        crate = state[from_stack].pop()
        state[to_stack].append(crate)

    return state


def apply_instruction9000(state: List[List[str]], instruction: str) -> List[List[str]]:
    split_instruction = instruction.split()
    quantity = int(split_instruction[1])
    from_stack = int(split_instruction[3]) - 1
    to_stack = int(split_instruction[5]) - 1

    intermediate_stack = []

    for i in range(quantity):
        if len(state[from_stack]) == 0:
            break
        crate = state[from_stack].pop()
        intermediate_stack.append(crate)

    for i in range(len(intermediate_stack)):
        state[to_stack].append(intermediate_stack.pop())

    return state


initial_state = parse_initial_state(initial_state_str)
final_state = reduce(apply_instruction, instructions, initial_state)
print("".join(["" if len(stack) == 0 else stack.pop() for stack in final_state]))

initial_state = parse_initial_state(initial_state_str)
final_state9000 = reduce(apply_instruction9000, instructions, initial_state)
print("".join(["" if len(stack) == 0 else stack.pop() for stack in final_state9000]))
