def solution(new_id):
    answer = ''
    new1 = []
    new2 = []
        
    new1 = new_id.lower()
            
    for i in new1:
        if i.isalnum() or i=='-' or i == '_' or i =='.':
            new2.append(i)
    new1= []
    for i,text in enumerate(new2):
        if text == '.': 
            if len(new1)>0 and new1[-1] == '.':
                continue
        new1.append(text)
    
    if len(new1)>0:
        if new1[0] == '.':
            del new1[0]
    if len(new1)>0:        
        if new1[-1] == '.':
            new1.pop()
    
    if len(new1) == 0:
        new1.append('a')
        
    if len(new1) >=16:
        new1  = new1[:15]
        if new1[-1] == '.':
            new1.pop()
    
    if len(new1)<3:
        while len(new1)<3:
            new1.append(new1[-1])
    
    return "".join(new1)