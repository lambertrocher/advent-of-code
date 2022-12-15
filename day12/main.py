from collections import defaultdict
from copy import copy
from pprint import pprint

from matplotlib.animation import FuncAnimation

from tabulate import tabulate

file = open("input.txt", "r")
lines = file.readlines()

width = len(lines[0].strip())
height = len(lines)

height_map = []
end = None
starts = []
for r in range(height):
    height_row = []
    for c in range(width):
        value = None
        if lines[r][c].islower() and lines[r][c] != "a":
            value = ord(lines[r][c]) - 96
        elif lines[r][c] == "S":
            starts.append((r, c))
            value = 0
        elif lines[r][c] == "a":
            starts.append((r, c))
            value = 1
        elif lines[r][c] == "E":
            end = (r, c)
            value = 26
        height_row.append(value)
    height_map.append(height_row)

# print(tabulate(height_map, tablefmt="none"))

graph = defaultdict(set)
for r in range(height):
    for c in range(width):
        if height_map[r][c] - height_map[r][c - 1] <= 1 and c > 0:
            graph[(r, c - 1)].add((r, c))
        if height_map[r][c-1] - height_map[r][c] <= 1 and c > 0:
            graph[(r, c)].add((r, c - 1))
        if height_map[r][c] - height_map[r - 1][c] <= 1 and r > 0:
            graph[(r - 1, c)].add((r, c))
        if height_map[r-1][c] - height_map[r][c] <= 1 and r > 0:
            graph[(r, c)].add((r - 1, c))

# pprint(graph)


def bfs(graph, start, end):
    queue = [[start]]
    visited = set()
    visited.add(start)
    visited_list = []
    visited_list.append(start)
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                visited_list.append(v)
                new_path = path + [v]
                queue.append(new_path)
                if v == end:
                    print("Path found: ", new_path)
                    return len(new_path) - 1
                    # return visited_list
    print("No path found")
    return 1000


res = [bfs(graph, start, end) for start in starts]
print(min(res))

# import matplotlib.pyplot as plt

# Define a 2D list of colors
# colors = height_map
#
# figure, ax = plt.subplots()
# im = ax.imshow(colors, interpolation='nearest', animated=True)
#
# def animate(i):
#     print("animate", i)
#     visited_r, visited_c = visited_list[i]
#     colors[visited_r][visited_c] = 40
#     im.set_data(colors)
#     return im
#
# ani = FuncAnimation(figure, animate, interval=1, frames=len(visited_list))
# plt.show()
