linesSearched = []
numberLocations = {}

f = open("2023\day4\input.txt", "r")
score = 0

for line in f:
    currLine = line.replace("\n","")[line.index(": ") + 2:].split(" | ")
    values = [section.replace("  ", " ").lstrip().split(" ") for section in currLine]

    same = list(set(values[0]).intersection(values[1]))
    if len(same) > 0:
        score += (2 ** (len(same) - 1))

    print(score)