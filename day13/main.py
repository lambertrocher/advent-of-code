import ast

file = open("input.txt", "r")
lines = file.read()

sequences = lines.split("\n\n")
sequences = [sequence.split("\n") for sequence in sequences]


def compare_packet(left, right):
    if not left and not right:
        return -1
    if not left:
        return 1
    if not right:
        return -1
    if type(left) == int and type(right) == int:
        return right - left
    if type(left) == int and type(right) != int:
        return compare_packet([left], right)
    if type(right) == int and type(left) != int:
        return compare_packet(left, [right])
    for la, r in zip(left, right):
        co = compare_packet(la, r)
        if co != 0:
            return co


result = 0
for index, sequence in enumerate(sequences):
    left = ast.literal_eval(sequence[0])
    right = ast.literal_eval(sequence[1])
    comp = compare_packet(left, right)
    print(comp)
    if comp > 0:
        print(index + 1)
        result += index + 1
print(result)
