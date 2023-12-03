def convertToPriority(char):
    ascii = ord(char)
    
    if(str.islower(char)):
        return ascii - 96
    else:
        return ascii - 65 + 27

def findSimilarity(lines):
    sharedChar = ''.join(set(lines[0]).intersection(lines[1]))
    sharedChar = ''.join(set(sharedChar).intersection(lines[2]))
    return sharedChar

    
f = open("2022\day3\input.txt", "r")
priorities = []
n = 1
currentGroup = []
for lines in f:
    currLine = lines.replace("\n", "")
    currentGroup.append(currLine)

    if n % 3 == 0:
        priorities.append(findSimilarity(currentGroup))
        currentGroup.clear()
                
    n += 1

values = [convertToPriority(c) for c in priorities]    
print(sum(values))

f.close()