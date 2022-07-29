import sys
input=sys.stdin.readline

num=int(input())
stack=[]

def solution(num):
    for _ in range(num):
        x=int(input())
        if x==0:
            stack.pop()
        else:
            stack.append(x)
    return sum(stack)

print(solution(num))

# sys 100ms / 3856ms