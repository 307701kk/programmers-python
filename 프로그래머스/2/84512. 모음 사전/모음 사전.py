def solution(word):
    answer = 0
    order = [781,156,31,6,1]
    gather = 'AEIOU'
    for i,w in enumerate(word):
        answer += order[i]*gather.index(w)+1
    return answer