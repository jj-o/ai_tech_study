import sys
input = sys.stdin.readline

def dfs(now,level,visited,distance):
    global answer,cutter
    if level == n:
        tmp = distance + abs(0 - now[0]) + abs(0 - now[1])
        answer = min(answer,tmp)
        cutter = answer
        print(answer)
    else:
        for i in range(len(s)):
            tmp = abs(now[0] - s[i][0]) + abs(now[1] - s[i][1])
            if visited[i] == False and distance + tmp < cutter:
                visited[i] = True
                # tmp = abs(now[0] - s[i][0]) + abs(now[1] - s[i][1])
                # print(tmp)
                dfs(s[i],level + 1,visited,distance + tmp)
                visited[i] = False

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    s = set()
    for _ in range(n):
        x,y = map(int,input().split())
        s.add((x,y))
    s = list(s)
    now2 = (0,0)
    cutter = sys.maxsize
    answer = sys.maxsize
    visited = [False]*n
    dfs(now2,0,visited,0)
    print(answer)