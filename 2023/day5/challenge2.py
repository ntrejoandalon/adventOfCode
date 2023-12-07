currentValues  = []
seperateBySections = []

def readInput():
    f = open("2023\day5\input.txt", "r")
    currentSection = []
    
    for line in f:
        currLine = line.replace("\n","")
        
        if len(currLine) > 0:
            currentSection.append(currLine)
        else:
            seperateBySections.append(currentSection)
            currentSection = []
    
    seperateBySections.append(currentSection)
    
    f.close()
    currentValues = seperateBySections[0][0][7:].split(" ")
    k = [line for line in [section[1:] for section in seperateBySections[1:]]]
    
    seperateBySections.clear()
    for layer in k:
        currentSection = []
        for row in layer:
            currentSection.append(row.split(" "))
            
        seperateBySections.append(currentSection)
        
    return currentValues

def mapToNewValues(layer, value):  
    n = 0
    found = False
    newVal = value
    
    while not found and n < len(layer):
        convertedValue, startVal, size = layer[n]
        diff = value - int(startVal)
        if (diff >= 0 and diff < int(size)):
            newVal = int(convertedValue) + diff
            found = True
        n += 1
            
    return newVal
          
currentValues = readInput()

values  = []
for i in range(int((len(currentValues) +1) / 2)):
    startVal = int(currentValues[i * 2])
    endVal = startVal + int(currentValues[(i*2) + 1])
    
    values.extend(list(range(startVal, endVal)))

for section in seperateBySections:
    currentValues = [mapToNewValues(section, int(value)) for value in values]
    
print(min(currentValues))
