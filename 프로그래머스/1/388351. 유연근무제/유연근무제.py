def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        day = startday
        people = schedules[i]
        
        hcut = people//100
        mcut = people - hcut*100
        if mcut>=50:
            hcut +=1 
            mcut -= 50
        else:
            mcut+=10
        box = True
        
        for j in range(7):
            today =  day%7
            day+=1  
            if today ==0 or today ==6:
                continue
            time = timelogs[i][j]
            h = time// 100
            m = time%100
            
            if h>hcut:
                box = False
                break
            elif h == hcut and m>mcut:
                box = False
                break 
        if box:
            answer+=1
    return answer