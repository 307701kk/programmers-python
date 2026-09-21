def solution(n, t, m, p):
    number = ''
    num = 0
    
    def jinsu(n,num):
        jin = ''
        su = [0,1,2,3,4,5,6,7,8,9,'A',"B",'C','D',"E",'F']
        while num>0:
            word = num%n
            num = num//n
            jin += str(su[word])
        if len(jin) == 0:
            return '0'
        jin = jin[::-1]
        return jin

    while len(number)<=(t*m):
        coding = jinsu(n,num)
        
        number += coding
        num +=1
    number = number[p-1::m]
    return number[:t]