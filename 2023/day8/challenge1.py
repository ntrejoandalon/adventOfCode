GIVEN_INSTRUCTION = []
instruction_queue= []
nodes = {}
currentNodes = []
f = open("2023\day8\input.txt", "r")

n = 0
for line in f:
    currLine = line.strip("\n")
    
    if n == 0:
        GIVEN_INSTRUCTION = [c for c in currLine]
        instruction_queue .extend(GIVEN_INSTRUCTION)
    elif n > 1:
        key = currLine[:3]
        values = currLine[7:len(currLine)-1].replace(" ", "").split(",")
        if key[-1] == 'A':
            currentNodes.append(key)
        
        nodes[key] = values
     
    n += 1
    
f.close()

numSteps = 0
atZ = 0
paths = []

for node in currentNodes:
    instruction_queue.clear()
    instruction_queue.extend(GIVEN_INSTRUCTION)
    instruction = 0 if instruction_queue.pop(0) == 'L' else 1

    currentNode = nodes[node][instruction]
    nodePath = [currentNode]
    
    while currentNode[-1] != 'Z':
        if len(instruction_queue) == 0:
            instruction_queue.extend(GIVEN_INSTRUCTION)
            
        instruction = 0 if instruction_queue.pop(0) == 'L' else 1
        currentNode = nodes[currentNode][instruction]
        nodePath.append(currentNode)
        
    paths.append(nodePath)
    
lengths = [len(path) for path in paths]
print(lengths)
print(len(GIVEN_INSTRUCTION))
