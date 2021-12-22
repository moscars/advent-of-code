seen = {}

def solveWins(p1, p2, p1Score, p2Score, p1Turn):
    if (p1, p2, p1Score, p2Score, p1Turn) in seen:
        return seen[(p1, p2, p1Score, p2Score, p1Turn)]

    if p1Score >= 21: return [1, 0]
    if p2Score >= 21: return [0, 1]
    
    p1wins = 0
    p2wins = 0
    for first in range(1, 4):
        for second in range(1, 4):
            for third in range(1, 4):
                tmp = first + second + third
                tmp += p1 if p1Turn else p2
                if tmp > 10:
                    tmp -= 10
                
                res = []
                if p1Turn:
                    res = solveWins(tmp, p2, p1Score + tmp, p2Score, False)
                else:
                    res = solveWins(p1, tmp, p1Score, p2Score + tmp, True)
                                        
                p1wins += res[0]
                p2wins += res[1]
    
    seen[(p1, p2, p1Score, p2Score, p1Turn)] = [p1wins, p2wins]
    return [p1wins, p2wins]
        
print(max(solveWins(7, 5, 0, 0, True)))
    
    
    