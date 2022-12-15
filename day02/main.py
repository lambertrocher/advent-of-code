# Open the file and read the strategy guide
with open('input.txt') as f:
    strategy_guide = f.readlines()


guide = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",

    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",

    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}
new_strategy_guide = []
for round in strategy_guide:
    round = round.rstrip()
    new_strategy_guide.append(guide[round])

print(new_strategy_guide)

shape_scores = {
    "X": 1,  # rock A
    "Y": 2,  # paper B
    "Z": 3  # scissors C
}

wins = {"C X","A Y","B Z"}

draws = {"A X", "B Y", "C Z"}

score = 0
for round in new_strategy_guide:
    if round in wins:
        score += 6
    elif round in draws:
        score += 3

    _, my_play = round.split()
    score += shape_scores[my_play]
print(score)
