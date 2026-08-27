def solution(A,B):
    answer = 0

    a = sorted(A)
    b = sorted(B)

    for i in range(len(A)):
        answer += a[i]*b[-(i+1)]
    return answer