def solution(n):
    answer = 0
    start, end = 1, 1
    num = 1
    
    while start <= n:
        if num < n:
            n_end = end + 1
            num += n_end
            end = n_end
        elif num == n:
            num -= start
            start += 1
            answer += 1
        else:
            num -= start
            start += 1
    return answer