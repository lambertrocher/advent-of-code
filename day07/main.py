import collections
from collections import defaultdict
from itertools import accumulate

with open('input.txt') as f:
    lines = f.readlines()

pwd = []
sizes = defaultdict(int)
bff = defaultdict(int)

for line in lines:
    line = line.strip()
    if line.startswith("$ ls") or line.startswith("dir"):
        continue
    elif line.startswith('$ cd ..'):
        pwd.pop()
    elif line.startswith('$ cd'):
        pwd.append(line.split()[2])
    else:
        for path in accumulate(pwd, func=lambda a, b: a + "/" + b):
            # print(path)
            sizes[path] += int(line.split()[0])
        for path in pwd:
            # print(path)
            bff[path] += int(line.split()[0])

print(sum(size for size in bff.values() if size <= 100_000))
print(min(size for size in sizes.values() if size >= sizes["/"] - 40_000_000))

