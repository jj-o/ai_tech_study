import sys
from collections import deque
import copy
input = sys.stdin.readline

def bfs(x,y):
    global visited,dx,dy
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<m and visited[xx][yy] == 0 and board[xx][yy] == 1:
                visited[xx][yy] = 1
                q.append((xx,yy))

tc = int(input().strip())
for _ in range(tc):
    m,n,k = map(int,input().split())
    board = [[0]*m for _ in range(n)]
    global visited,dx,dy
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    visited = copy.deepcopy(board)
    answer = 0
    for _ in range(k):
        y,x = map(int,input().split())
        board[x][y] = 1
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and board[i][j] == 1:
                answer += 1
                bfs(i,j)
    print(answer)