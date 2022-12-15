# with open("input.txt", "r") as f:
#     total_priority = 0
#     for line in f:
#         line_length = len(line)
#         half_length = line_length // 2
#         first_string = line[:half_length]
#         second_string = line[half_length:]
#         common_letter = None
#         for char in first_string:
#             if char in second_string:
#                 common_letter = char
#                 break
#         priority = None
#         if common_letter.islower():
#             priority = ord(common_letter) - 97 + 1
#         elif common_letter.isupper():
#             priority = ord(common_letter) - 65 + 26 + 1
#         total_priority += priority
#     print("Somme des priorités:", total_priority)

from string import ascii_letters

print(ascii_letters.index("A") + 1)