def solution(k, dungeons):
    answer,count = 0,0
    check = [0]*len(dungeons)
    
    def travel(k,count):
        nonlocal answer
        answer = max(answer,count)
        
        for i,dungeon in enumerate(dungeons):
            cut,hp = dungeon
            if check[i] == 0:
                if k>=cut:
                    check[i] = 1
                    travel(k- hp,count+1)
                    check[i] = 0  
    
    travel(k,answer) 
    return answer


    