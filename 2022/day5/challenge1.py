import re

boxes = []
boxLines = []
insturctions = []
overlapping = 0
    
def breakLines():
    onBoxes = True
    f = open("2022\day5\input.txt", "r")

    for line in f:
        currLine = line.replace("\n", "")
        
        if len(currLine) == 0:
            onBoxes = False
        elif onBoxes:
            boxLines.append(currLine)
        else: 
            words = currLine.split(" ")
            insturctions.append([int(num) for num in words if num.isnumeric()])
    
    f.close()
            
def establishBoxStacks():
    numbers = [int(val) for val in (boxLines[-1].replace(" ", ",")).split(",") if val != '']
    boxes = [ [] for _ in range(numbers[-1]) ]

    for line in boxLines[:-1]:
        col = 0
        while col < numbers[-1]:
            letterVal = line[col * 4 + 1]
            if (letterVal != " "):
                boxes[col].append(letterVal)                
            col += 1
            
    return boxes
       
def followInstruction(task):
    #amount, start, end
    amount, start, end = task[0], task[1] - 1, task[2] -1
    for i in range(amount):
        value = boxes[start].pop(0)
        boxes[end].insert(0, value)
    return boxes
    

    
breakLines()
boxes = establishBoxStacks()
for instruction in insturctions:
    boxes = followInstruction(instruction)

topBoxes = "".join([stack[0] for stack in boxes])
print(topBoxes)