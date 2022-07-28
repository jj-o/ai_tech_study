from collections import deque
import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[b][a] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >=n :
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx,ny))

t = int(input())
for i in range(t):
    cnt=0
    m, n, k = map(int,sys.stdin.readline().strip().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int,sys.stdin.readline().strip().split())
        graph[y][x] = 1

    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                bfs(graph, a, b)
                cnt+=1

    print(cnt)