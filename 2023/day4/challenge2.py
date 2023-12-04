linesSearched = []
numberLocations = {}

f = open("2023\day4\input.txt", "r")
numScratches = 0
copyQueue = [0]

def distributeCopies(numCopies, sameSet):
    winValue = 1 + numCopies
    for i in range(len(sameSet)):
        if i < len(copyQueue):
            copyQueue[i] += winValue
        else:
            copyQueue.append(winValue)    
    
    return copyQueue

for line in f:
    numberCopies = copyQueue.pop(0) if len(copyQueue) > 0 else 0
    
    currLine = line.replace("\n","")[line.index(": ") + 2:].split(" | ")
    values = [section.replace("  ", " ").lstrip().split(" ") for section in currLine]

    same = list(set(values[0]).intersection(values[1]))
    copyQueue = distributeCopies(numberCopies, same)
        
    numScratches+= 1 + numberCopies

print(numScratches)