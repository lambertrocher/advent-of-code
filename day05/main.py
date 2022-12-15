from collections import defaultdict

file = open("input.txt")
contents = file.read()

crates, moves = contents.split("move")[0], contents.split("move")[1:]

stacks = defaultdict(list)
for line in crates.split("\n"):
    crate_line = [line[i+1:i+2].strip() for i in range(0, len(line), 4)]
    if not crate_line or crate_line[0].isdigit():
        break
    for i, crate in enumerate(crate_line):
        if crate:
            stacks[i].insert(0, crate)

for move in moves:
    move = move.split()
    temp_stack = []
    for _ in range(int(move[0]),0,-1):
        crate = stacks[int(move[2])-1].pop()
        temp_stack.append(crate)
    stacks[int(move[4])-1].extend(temp_stack[::-1])

stacks = dict(sorted(stacks.items()))
result = "".join(stack[-1] for stack in stacks.values())
print(result)
