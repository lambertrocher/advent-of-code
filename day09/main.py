file = open("input.txt", "r")
lines = file.readlines()

hx, hy = 1, 1
tx, ty = 1, 1

x_max, y_max = 600000, 500000
x_min, y_min = -1000000, -1000000

tpos = set()
tpos.add((tx, ty))
print(tpos)

def move_tail(tx, ty, hx, hy):
    if tx < hx and ty < hy and not (tx == hx-1 and ty == hy-1):
        tx += 1
        ty += 1
    elif tx < hx and ty > hy and not (tx == hx-1 and ty == hy+1):
        tx += 1
        ty -= 1
    elif tx > hx and ty < hy and not (tx == hx+1 and ty == hy-1):
        tx -= 1
        ty += 1
    elif tx > hx and ty > hy and not (tx == hx+1 and ty == hy+1):
        tx -= 1
        ty -= 1
    elif tx < hx - 1:
        tx += 1
    elif tx > hx + 1:
        tx -= 1
    elif ty < hy - 1:
        ty += 1
    elif ty > hy + 1:
        ty -= 1
    return tx, ty

for line in lines:
    direction, distance = line[0], int(line[1:])
    for _ in range(distance):
        if direction == "U":
            hy = min(y_max, hy + 1)
        elif direction == "D":
            hy = max(y_min, hy - 1)
        elif direction == "R":
            hx = min(x_max, hx + 1)
        elif direction == "L":
            hx = max(x_min, hx - 1)
        tx, ty = move_tail(tx, ty, hx, hy)
        print("-----")
        print(hx, hy)
        print(tx, ty)
        tpos.add((tx, ty))

print(tpos)
print(len(tpos))



sgn = lambda x: (x > 0) - (x < 0)
R = [(0, 0) for _ in range(10)]
D, Seen = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}, {R[-1]}
file = open("input.txt", "r")
lines = file.readlines()
for line in lines:
    d, v = line[0], int(line[1:])
    for _ in range(v):
        R[0] = tuple(sum(x) for x in zip(R[0], D[d]))
        for i in range(1, len(R)):
            dx, dy = R[i-1][0] - R[i][0], R[i-1][1] - R[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                R[i] = tuple(sum(x) for x in zip(R[i], [sgn(dx), sgn(dy)]))
        Seen.add(R[-1])

print(len(Seen))