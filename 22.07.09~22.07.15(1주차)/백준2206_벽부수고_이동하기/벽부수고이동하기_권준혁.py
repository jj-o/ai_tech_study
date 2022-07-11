import sys
from collections import deque
input = sys.stdin.readline

# 입력값 지정
n,m = map(int,input().split())
board = [list(int(num) for num in input().strip()) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
q = deque()

# solution 함수
def solution(n,m,board):
    q.append((0,0,0))
    visited[0][0][0] = 1
    while(q):
        x,y,w = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<m and board[xx][yy] == 0 and visited[xx][yy][w] == 0:
                visited[xx][yy][w] = visited[x][y][w] + 1
                q.append((xx,yy,w))
            if 0<=xx<n and 0<=yy<m and board[xx][yy] == 1 and w == 0:
                visited[xx][yy][1] = visited[x][y][0] + 1
                q.append((xx,yy,1))
    return -1
print(solution(n,m,board))