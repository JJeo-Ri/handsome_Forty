def solution(board, moves):
    bag = [0]
    count = 0
    
    for move in moves:
        for row in board:
            if row[move-1] == 0:
                continue
                
            picked = row[move-1]
            row[move-1] = 0
            
            if picked == bag[-1]:
                bag.pop()
                count += 2
                break
                
            bag.append(picked)
            break
    
    return count