import re
import matplotlib.pyplot as plt


def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))


file = open("input.txt", "r")
lines = file.readlines()


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


x_max = y_max = 400000


# search_line = 2000000

# for search_line in range(0, y_max):
#     print(search_line)
#     covered = set()
#     for line in lines:
#         numbers = ints(line)
#         sensor = (numbers[0], numbers[1])
#         beacon = (numbers[2], numbers[3])
#         beacon_distance = manhattan(sensor[0], sensor[1], beacon[0], beacon[1])
#         for x1 in range(max(sensor[0]-beacon_distance, 0), min(sensor[0]+beacon_distance+1, x_max)):
#             if manhattan(x1, search_line, sensor[0], sensor[1]) <= beacon_distance:
#                 # if (x1, search_line) != (beacon[0], beacon[1]):
#                 covered.add(x1)
#     for t in range(0, x_max):
#         if t not in covered:
#             print(t*400000 + search_line)
#             exit()
# print(covered)
# print(len(covered))

def is_inside_range(cell, sensors):
    for sensor in sensors:
        if manhattan(cell[0], cell[1], sensor[0], sensor[1]) <= sensor[2]:
            return True
    return False


covered = set()
sensors = set()
for line in lines:
    numbers = ints(line)
    beacon = (numbers[2], numbers[3])
    sensor_x, sensor_y = numbers[0], numbers[1]
    sensor = (sensor_x, sensor_y, manhattan(sensor_x, sensor_y, beacon[0], beacon[1]))
    sensors.add(sensor)

for sensor in sensors:
    print(sensor)
    sensor_outline = sensor[2] + 1
    outline = []
    for x in range(0, sensor_outline):
        outline.append((sensor[0] + x, sensor[1] + sensor_outline - x))
        outline.append((sensor[0] + x, sensor[1] - sensor_outline + x))
        outline.append((sensor[0] - x, sensor[1] + sensor_outline - x))
        outline.append((sensor[0] - x, sensor[1] - sensor_outline + x))
    # x, y = zip(*outline)
    # plt.plot(x, y)
    # plt.show()
    for cell in outline:
        if not 0 < cell[0] < 4000000 or not 0 < cell[1] < 4000000:
            continue
        is_hidden = True
        if not is_inside_range(cell, sensors):
            print("cell is hidden", cell)
            print(cell[0] * 4000000 + cell[1])
            exit(0)


print("done")
