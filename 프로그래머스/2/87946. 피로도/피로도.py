from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        
        for cut, use in p:
            if hp >= cut:
                hp -= use
                count += 1
            else:
                break
                
        answer = max(answer, count)
        
    return answer