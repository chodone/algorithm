def pair(participants):
    
    partNum = set(participants)
    
    
    for num in partNum:
        cnt = 0
        for j in participants:
            if num == j:
                cnt += 1
        if cnt == 2:
            participants.remove(num)
            participants.remove(num)
                
    return participants
            
            
                
        
            
         




participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
print(pair(participants))