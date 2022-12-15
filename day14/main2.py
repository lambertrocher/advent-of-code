from pprint import pprint

file = open("input.txt", "r")
lines = file.readlines()

terrain = {}

for line in lines:
    paths = line.strip().split(" -> ")
    paths = [(int(path.split(",")[0]), int(path.split(",")[1])) for path in paths]
    p0 = paths[0]
    for p1 in paths[1:]:
        if p0[0] == p1[0]:
            for y in range(min(p0[1], p1[1]), max(p0[1], p1[1]) + 1):
                terrain[(p0[0], y)] = "#"
        elif p0[1] == p1[1]:
            for x in range(min(p0[0], p1[0]), max(p0[0], p1[0]) + 1):
                terrain[(x, p0[1])] = "#"
        p0 = p1
pprint(terrain)

abyss = max(terrain.keys(), key=lambda x: x[1])[1] + 2
print(abyss)

result = 0
sand_source = (500, 0)
while True:
    if sand_source in terrain:
        print("IT'S DONE")
        print(terrain)
        print(result)
        exit(0)
    sand_block = sand_source
    while True:
        if sand_block[1] >= abyss:
            terrain[sand_block] = "s"
            break
        if (sand_block[0], sand_block[1] + 1) not in terrain:
            sand_block = (sand_block[0], sand_block[1] + 1)
            continue
        if (sand_block[0] - 1, sand_block[1] + 1) not in terrain:
            sand_block = (sand_block[0] - 1, sand_block[1] + 1)
            continue
        if (sand_block[0] + 1, sand_block[1] + 1) not in terrain:
            sand_block = (sand_block[0] + 1, sand_block[1] + 1)
            continue
        terrain[sand_block] = "s"
        result += 1
        # print(terrain)
        break
