import sys
input = sys.stdin.readline
from collections import deque

# 입력값 지정
n,m = map(int,input().split())
board = [list(int(num) for num in input().strip()) for _ in range(n)]

def bfs() -> int:
    global visited,dx,dy
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while(q):
        x,y,crashed = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crashed]
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            # 만약 xx,yy가 영역 내에 있다면
            if 0<=xx<n and 0<=yy<m:
                # 만약 다음 칸이 벽이 아니라면
                if board[xx][yy] == 0 and visited[xx][yy][crashed] == 0:
                    visited[xx][yy][crashed] = visited[x][y][crashed] + 1
                    q.append((xx,yy,crashed))
                # 만약 다음 칸이 벽이라면
                elif board[xx][yy] == 1 and visited[xx][yy][crashed] == 0:
                    # crashed == 1: 이전에 벽을 부쉈기 때문에 벽을 부수지 않는다.
                    if crashed == 1:
                        continue
                    # crashed == 0: 이전에 벽을 안 부쉈기 때문에 벽을 부순다.
                    elif crashed == 0:
                        visited[xx][yy][1] = visited[x][y][crashed] + 1
                        q.append((xx,yy,1))
    return -1

# solution 함수
def solution(n,m,board):
    global visited,dx,dy
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    answer = 0
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    answer = bfs()
    return answer

print(solution(n,m,board))
