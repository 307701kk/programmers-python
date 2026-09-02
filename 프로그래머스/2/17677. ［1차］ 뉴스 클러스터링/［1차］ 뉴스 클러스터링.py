def solution(str1, str2):
    box1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    box2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    gyo = 0
    for i in box1:
        if i in box2:
            gyo += 1
            box2.remove(i)
            
    hap = len(box1) + len(box2)
    
    return int((gyo / hap) * 65536) if hap != 0 else 65536