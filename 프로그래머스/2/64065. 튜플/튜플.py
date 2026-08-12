def solution(s):
    answer = []
    s = s[2:len(s)-2]
    s = s.split('},{')
    s.sort(key = len)
    
    for i in s:
        box = i.split(',')
        for text in box:
            if int(text) not in answer:
                answer.append(int(text))
    return answer