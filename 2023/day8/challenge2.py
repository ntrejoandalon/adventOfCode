import re

GIVEN_INSTRUCTION = []
instruction_queue= []
nodes = {}
f = open("2023\day8\example.txt", "r")

n = 0
for line in f:
    currLine = line.strip("\n")
    
    if n == 0:
        GIVEN_INSTRUCTION = [c for c in currLine]
        instruction_queue .extend(GIVEN_INSTRUCTION)
    elif n > 1:
        key = currLine[:3]
        values = currLine[7:len(currLine)-1].replace(" ", "").split(",")
        
        if key != 'ZZZ':
            nodes[key] = values    
    n += 1
    
f.close()

attemptedNodes = 0
currentNode = 'AAA'

while currentNode != 'ZZZ':
    if len(instruction_queue) == 0:
        instruction_queue.extend(GIVEN_INSTRUCTION)
        
    instruction = 0 if instruction_queue.pop(0) == 'L' else 1
    currentNode = nodes[currentNode][instruction]
    attemptedNodes += 1
    
print(attemptedNodes)
