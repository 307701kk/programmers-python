def solution(numbers):
    answer = [-1]*len(numbers)
    
    stay = []
    for i,number in enumerate(numbers):
        while len(stay)!=0 and numbers[stay[-1]]<number:
            num = stay.pop()
            answer[num] = numbers[i]
        stay.append(i)
    return answer