from enum import IntEnum

VALUE_RANKING = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3','2']

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
        
    def determineType(self):
        noDuplicates = set(self.value)
        noDuplicatesLen = len(noDuplicates)
        
        if noDuplicatesLen == 2:
            for c in noDuplicates:
                result = len(''.join(ch for ch in self.value if ch == c))
                if result == 4:
                    return HandType.FOUR_KIND

            return HandType.FULL_HOUSE
        elif noDuplicatesLen == 3: 
            for c in noDuplicates:
                result = len(''.join(ch for ch in self.value if ch == c))
                if result == 3:
                    return HandType.THREE_KIND
            
            return HandType.TWO_PAIR
        elif noDuplicatesLen == 4:
            return HandType.ONE_PAIR
        elif noDuplicatesLen == 5:
            return HandType.HIGH_CARD
        
    
        return HandType.FIVE_KIND
    
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
