# 풀이1
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
    
    
# 풀이2
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# Test Case 수 T 입력
t = int(input())

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# x : 행, y : 열
def dfs(graph, x, y):
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            if graph[nx][ny] == 1:
                dfs(graph, nx, ny)
    return

for i in range(t):
    # 가로 길이 M, 세로 길이 N, 배추가 심어져있는 위치의 개수 K 입력
    m, n, k = map(int, input().split())
    # 배추 graph 및 방문 여부 list 생성
    graph = [ [0] * m for _ in range(n) ]

    # 배추 위치값 입력받기
    for i in range(k):
        m_v, n_v = map(int, input().split())
        graph[n_v][m_v] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                cnt += 1
    print(cnt)