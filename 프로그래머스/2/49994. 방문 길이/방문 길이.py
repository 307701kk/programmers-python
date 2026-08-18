def solution(dirs):
    control = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}
    x,y = 0,0
    street = set()
    for i in dirs:
        dx,dy = control[i]
        nx,ny = x+dx,y+dy
        
        if -5<=nx<=5 and -5<=ny<=5:
            path = tuple(sorted([(x,y),(nx,ny)]))
            street.add(path)
            x,y = nx,ny
    return len(street)