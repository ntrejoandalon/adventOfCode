f = open("2022\day3\input.txt", "r")
priorities = []

def determineSharedValue(line):
    pt1 = line[:int(len(line) / 2)]
    pt2 = line[int(len(line) / 2):]
    sharedChar = ''.join(set(pt1).intersection(pt2))
    return sharedChar

def convertToPriority(char):
    ascii = ord(char)
    
    if(str.islower(char)):
        return ascii - 96
    else:
        return ascii - 65 + 27
    
for lines in f:
    currLine = lines.replace("\n", "")
    typeItem = determineSharedValue(currLine)
    priorities.append(convertToPriority(typeItem))
    
print(sum(priorities))
f.close()