from datetime import datetime

file = open("input.txt", "r")
input = file.read()
print(input)

for i in range(len(input)-14):
    if len(set(input[i:i+14])) == 14:
        print(i+14)
        break
