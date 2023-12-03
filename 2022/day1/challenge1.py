f = open("2022\day1\input.txt", "r")
elfLists = [0]
n = 0

for lines in f:
    if len(lines) == 1 and lines[0] == '\n':
        n += 1
        elfLists.append(0)
    else:
        elfLists[n] = elfLists[n] + int(lines[:len(lines)-1])

print(max(elfLists))
f.close()