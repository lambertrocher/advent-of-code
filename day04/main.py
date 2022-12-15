file = open("input.txt")
contents = file.read()
pairs = contents.split("\n")

counter = 0
not_overlaps = 0
for pair in pairs:
    elf1, elf2 = pair.split(",")
    elf1_min, elf1_max = elf1.split("-")
    elf2_min, elf2_max = elf2.split("-")
    elf1_min, elf1_max, elf2_min, elf2_max = int(elf1_min), int(elf1_max), int(elf2_min), int(elf2_max)
    if pair == "9-89,13-90":
        print(elf1_min, elf1_max, elf2_min, elf2_max)
    if (elf1_min <= elf2_min and elf1_max >= elf2_max) or (elf2_min <= elf1_min and elf2_max >= elf1_max):
        counter += 1
    if elf2_max < elf1_min or elf1_max < elf2_min:
        not_overlaps += 1
print(counter)
print(len(pairs) - not_overlaps)

