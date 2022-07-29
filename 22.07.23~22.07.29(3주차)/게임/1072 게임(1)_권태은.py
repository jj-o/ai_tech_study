
x,y=map(int,input().split())

def solution(x,y):
    result=0
    z=y*100//x
    lt,rt=0,x
    while lt<rt:
        m=(lt+rt)//2
        if (y+m)*100//(x+m)>z:
            result=m
            rt=m-1
        else:
            lt=m+1
    return result

print(solution(x,y))
            