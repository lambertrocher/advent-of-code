with open("input.txt", "r") as input:
    cals = []
    cal = 0
    for line in input:
        line = line.rstrip()
        if line:
            cal += int(line)
        else:
            cals.append(cal)
            cal = 0
    cals.append(cal)

cals.sort()
print(cals[-1])
print(cals[-1] + cals[-2] + cals[-3])
