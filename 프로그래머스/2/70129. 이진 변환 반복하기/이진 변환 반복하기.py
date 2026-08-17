def solution(s):
    zero = 0
    count = 0
    while len(s)>1:
        answer = ''
        for i in s:
            if i =='1':
                answer +=i
            else:
                zero +=1
        count+=1
        
        num = len(answer)
        s = str(bin(num)[2:])
        
    return [count,zero]