def solution(people, limit):
    answer = 0
    start,end = 0,len(people)-1
    people  = sorted(people)
    
    while start<=end :
        little,fat = people[start],people[end]
        if little+fat>limit:
            end -=1
            answer +=1
        else:
            start+=1
            end-=1
            answer +=1

    return answer