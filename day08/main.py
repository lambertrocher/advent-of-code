input = open("input.txt", "r")
lines = input.readlines()
trees = [list(line.strip()) for line in lines]
print(trees)

visible_trees = set()
for i in range(len(trees)):
    last_tree = trees[i][0]
    for j in range(len(trees[i])):
        if trees[i][j] > last_tree or j == 0:
            visible_trees.add((i, j))
            last_tree = trees[i][j]

for i in range(len(trees)):
    last_tree = trees[i][len(trees)-1]
    for j in reversed(range(len(trees[i]))):
        if trees[i][j] > last_tree or j == len(trees)-1:
            visible_trees.add((i, j))
            last_tree = trees[i][j]

for j in range(len(trees[0])):
    last_tree = trees[0][j]
    for i in range(len(trees)):
        if trees[i][j] > last_tree or i == 0:
            visible_trees.add((i, j))
            last_tree = trees[i][j]

for j in range(len(trees[0])):
    last_tree = trees[len(trees[0])-1][j]
    for i in reversed(range(len(trees))):
        if trees[i][j] > last_tree or i == len(trees[0])-1:
            visible_trees.add((i, j))
            last_tree = trees[i][j]


lenI = len(trees)
lenJ = len(trees[0])


def get_score(i0, j0):
    score1 = 0
    for i in range(i0+1, lenI):
        score1 += 1
        if trees[i][j0] >= trees[i0][j0]:
            break

    score2 = 0
    for i in reversed(range(0, i0)):
        score2 += 1
        if trees[i][j0] >= trees[i0][j0]:
            break

    score3 = 0
    for j in range(j0+1, lenJ):
        score3 += 1
        if trees[i0][j] >= trees[i0][j0]:
            break

    score4 = 0
    for j in reversed(range(0, j0)):
        score4 += 1
        if trees[i0][j] >= trees[i0][j0]:
            break

    return score1 * score2 * score3 * score4


print(max([get_score(i, j) for i in range(lenI) for j in range(lenJ)]))


