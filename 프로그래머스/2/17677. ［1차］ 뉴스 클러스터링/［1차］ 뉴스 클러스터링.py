def solution(str1, str2):
    box1,box2,box = [],[],[]
    gyo,hap = 0,0
    
    for i in range(len(str1)-1):
        word = str1[i]+str1[i+1]
        if word.isalpha():
            word = word.lower()
            box1.append(word)
    for i in range(len(str2)-1):
        word = str2[i]+str2[i+1]
        if word.isalpha():
            word = word.lower()
            box2.append(word)
    for i in box1:
        if i in box2:
            box.append(i)
            box2.remove(i)
    gyo = len(box)
    hap = len(box1) +len(box2) 
    
    return int ( (gyo/hap)*65536) if hap!=0 else 65536