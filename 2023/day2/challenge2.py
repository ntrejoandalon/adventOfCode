#GOAL. GET THE NUMBERS ON EACH LINE AND ADD TOGETHER

f = open("day2\input.txt", "r")
powers = []


def compileLineValues(line): 
    line = line.replace(', ',',')
    seperated = line.split("; ")
    setDictionaries = []

    for section in seperated:
        dictionary = dict(subString.split(" ")[::-1] for subString in section.split(","))
        dictionary = {k:int(v) for k,v in dictionary.items()}
        setDictionaries.append(dictionary)
        
    gameDict = {}    
    for i in range(len(setDictionaries)):
        currDict = setDictionaries[i]
        for key in currDict:
            if key not in gameDict or currDict[key] > gameDict[key]:
                gameDict[key] = currDict[key]

    return gameDict

    
def calculatePower(dictionary):
    power = 1
    for key in dictionary:
        power *= dictionary[key]
        
    return power
    
currentGame = 0
for line in f:
    currLine = line.replace('\n', '')
    currentGame += 1
    setInfo = currLine[currLine.index(":") + 2:len(currLine)]
    gameMaxes = compileLineValues(setInfo)
    powers.append(calculatePower(gameMaxes))
        
print(sum(powers))  
f.close()