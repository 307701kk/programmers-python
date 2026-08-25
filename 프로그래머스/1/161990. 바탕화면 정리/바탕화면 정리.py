def solution(wallpaper):
    answer = []
    file = []
    for x,col in enumerate(wallpaper):
        for y,i in enumerate(col):
            if i =='#':
                file.append((x,y))
    smallx,smally = file[0]
    maxx,maxy = file[0]
    for lux,luy in file:
        if lux < smallx:
            smallx = lux
        elif lux>maxx:
            maxx = lux
        if luy < smally:
            smally = luy
        elif luy>maxy:
            maxy = luy
    return [smallx,smally,maxx+1,maxy+1]