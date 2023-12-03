#GOAL. GET THE NUMBERS ON EACH LINE AND ADD TOGETHER

f = open("day2\input.txt", "r")
possibleGames = []
maxes = {"red" : 12, "green" : 13, "blue": 14}

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

def determineEligible(gameDictionary: dict): 
    eligible = True;
    for key in maxes:
        if (maxes[key] < gameDictionary[key]):
            eligible = False;
        
    return eligible
    
currentGame = 0
for line in f:
    currLine = line.replace('\n', '')
    currentGame += 1
    setInfo = currLine[currLine.index(":") + 2:len(currLine)]
    gameMax = compileLineValues(setInfo)
    if determineEligible(gameMax):
        possibleGames.append(currentGame)
        
        
print(sum(possibleGames))  
f.close()