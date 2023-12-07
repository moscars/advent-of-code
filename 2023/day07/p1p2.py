from collections import defaultdict
lines = open(0).read().splitlines()

mp = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10
}

def getType(cards):
    if len(cards) == 0:
        return 8
    
    cnts = defaultdict(int)
    for c in cards:
        cnts[c] += 1

    if 5 in cnts.values():
        return 1
    elif 4 in cnts.values():
        return 2
    elif 3 in cnts.values() and 2 in cnts.values():
        return 3
    elif 3 in cnts.values():
        return 4
    elif 2 in cnts.values():
        num2s = 0
        for v in cnts.values():
            if v == 2:
                num2s += 1
        if num2s == 2:
            return 5
        else:
            return 6
    else:
        return 7

class Hand:
    def __init__(self, cards, bid, t):
        self.cards = cards
        self.bid = bid
        self.t = t

    def __lt__(self, other):
        if self.t == other.t:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    my = self.cards[i]
                    ot = other.cards[i]

                    my = mp[my] if my in mp else int(my)
                    ot = mp[ot] if ot in mp else int(ot)

                    return my > ot
                    
        return self.t < other.t
    
    def improve(self):
        for c in self.cards:
            if c == "J":
                self.t = self.improveOne()
    
    def improveOne(self):
        if self.t == 1:
            assert False
        elif self.t == 2:
            return 1
        elif self.t == 3:
            assert False
        elif self.t == 4:
            return 2
        elif self.t == 5:
            return 3
        elif self.t == 6:
            return 4
        elif self.t == 7:
            return 6
        elif self.t == 8:
            return 7
    
handsP1 = []
handsP2 = []
for line in lines:
    c, bd = line.split()
    handsP1.append(Hand(c, int(bd), getType(c)))
    handsP2.append(Hand(c, int(bd), getType([c for c in c if c != "J"])))
    handsP2[-1].improve()

handsP1.sort(reverse=True)
mp['J'] = 0
handsP2.sort(reverse=True)

p1, p2 = 0, 0
for i, h in enumerate(handsP1):
    p1 += ((i+1) * h.bid)
    p2 += ((i+1) * handsP2[i].bid)

print(p1)
print(p2)