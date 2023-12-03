f = open("2022\day1\input.txt", "r")
elfLists = [0]
n = 0

for lines in f:
    currLine = lines.replace("\n", "")
    if len(currLine) == 0:
        n += 1
        elfLists.append(0)
    else:
        elfLists[n] = elfLists[n] + int(currLine)

elfLists.sort(reverse=True)
print(sum(elfLists[:3]))
f.close()