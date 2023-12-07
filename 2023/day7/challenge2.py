from enum import IntEnum

VALUE_RANKING = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3','2', 'J']

class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7
 
class Hand():    
    def __init__(self, cardValue):
        self.value = cardValue
        self.hand = self.determineType()
        
    def mapToNewValues(self, numJs, handType):
        adjustedType = handType

        if handType != HandType.FIVE_KIND:
            for i in range(numJs):
                if (adjustedType == HandType.HIGH_CARD or adjustedType == HandType.FOUR_KIND):
                    adjustedType = HandType(int(adjustedType) + 1)
                else: 
                    adjustedType = HandType(int(adjustedType) + 2)
        
        return adjustedType
        
    def determineType(self):
        numJ = len(''.join(ch for ch in self.value if ch == 'J'))
        repetitions = []
        uniqueChars = set("".join(ch for ch in self.value if ch != "J"))
        for c in uniqueChars: 
            repetitions.append(len("".join(ch for ch in self.value if ch == c)))
            
        value = None
        
        if len(repetitions) == 0 or 5 in repetitions: 
            value =  HandType.FIVE_KIND
        elif 4 in repetitions:
            value = HandType.FOUR_KIND
        elif 3 in repetitions and 2 in repetitions:
            value = HandType.FULL_HOUSE
        elif 3 in repetitions:
            value = HandType.THREE_KIND
        elif repetitions.count(2) == 2:
            value = HandType.TWO_PAIR
        elif 2 in repetitions:
            value = HandType.ONE_PAIR
        else:
            value = HandType.HIGH_CARD
        
        newVal = self.mapToNewValues(numJ, value) if value != HandType.FIVE_KIND and value != HandType.FULL_HOUSE else value

        return newVal
    
    def compareHands(self, second):   
        typeComparison = self.hand > second.hand
        
        n = 0
        greater = typeComparison
        if self.hand == second.hand:
            while self.value[n] == second.value[n]:
                n += 1
            
            greater = (VALUE_RANKING.index(self.value[n]) < VALUE_RANKING.index(second.value[n]))
            
        return greater

    def __lt__(self, obj): 
        return (not self.compareHands(obj)) 
  
    def __repr__(self): 
        return str((self.value, self.hand))  

cards= []
f = open("2023\day7\input.txt", "r")

for line in f:
    currLine = line.strip("\n")
    seperation  = currLine.split(" ")
    cards.append((Hand(seperation[0]), int(seperation[1])))
f.close()

sorted_l = sorted(cards)
for value in sorted_l:
    print(value)
    
bids = [value[1] for value in sorted_l]
ranking = list(range(1, len(bids) +1))
res_list = list(map(lambda x, y: x * y, bids, ranking))

print(sum(res_list))

