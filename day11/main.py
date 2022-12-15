import math
from dataclasses import dataclass
import re

file = open("input.txt", "r")
input_file = file.read()


@dataclass
class Monkey:
    id: int
    items: list[int]
    operation: str
    test: int
    throw_true: int
    throw_false: int
    inspected: int = 0

def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))


monkeys = []

for monkey in input_file.split("\n\n"):
    lines = monkey.splitlines()
    monkeys.append(
        Monkey(
            id=ints(lines[0])[0],
            items=ints(lines[1]),
            operation=lines[2].split("=")[-1],
            test=ints(lines[3])[-1],
            throw_true=ints(lines[4])[-1],
            throw_false=ints(lines[5])[-1],
        )
    )

k = math.prod(m.test for m in monkeys)
for round in range(10000):
    # print(round)
    # print(monkeys)
    for monkey in monkeys:
        for item in monkey.items:
            item = eval(f"{monkey.operation.replace('old', 'item')}")
            monkey.inspected += 1
            # item = int(item / 3)
            item = item % k
            if item % monkey.test == 0:
                monkeys[monkey.throw_true].items.append(item)
            else:
                monkeys[monkey.throw_false].items.append(item)
        monkey.items.clear()
    #
    # print(f"--------- round {round} -------")
    # for monkey in monkeys:
    #     print(f"{monkey.id}: {monkey.items}")

monkeys.sort(key=lambda x: x.inspected)
print(monkeys[-1].inspected * monkeys[-2].inspected)
