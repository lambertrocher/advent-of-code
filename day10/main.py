input = open("input.txt", "r")
lines = input.readlines()

x = 1
cycle = 0
result = 0
crt = []
for line in lines:
    line = line.strip()
    if line == "noop":
        cycle += 1
        print(cycle)
        crt_x = cycle % 40 - 1
        if abs(x-crt_x) <=1:
            crt.append("#")
        else:
            crt.append(" ")
        if cycle % 40 == 20:
            result += cycle*x
    else:
        cycle += 1
        print(cycle)
        crt_x = cycle % 40 - 1
        if abs(x - crt_x) <= 1:
            crt.append("#")
        else:
            crt.append(" ")
        if cycle % 40 == 20:
            result += cycle*x
        cycle += 1
        print(cycle)
        crt_x = cycle % 40 - 1
        if abs(x - crt_x) <= 1:
            crt.append("#")
        else:
            crt.append(" ")
        if cycle % 40 == 20:
            result += cycle*x
        val = int(line.split()[1])
        x += val
    # print(x)

print(result)
cr = [crt[i:i + 40] for i in range(0, len(crt), 40)]
for l in cr:
    print("".join(l))