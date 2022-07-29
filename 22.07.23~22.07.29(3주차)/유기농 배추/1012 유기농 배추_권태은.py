'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''

import sys
from collections import deque
input=sys.stdin.readline

def bfs(y,x):
    # 리스트를 사용하면 시간복잡도가 O(N)인데 반하여,
    # deque를 사용하면 시간복잡도가 0(1)이다
    q=deque()
    q.append((y,x))    
    while q:
        x,y=q.popleft()
        print((x,y))
        for i in range(4):
            global dx, dy
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<width and 0<=yy<height and field[yy][xx]==1:
                field[yy][xx]-=1
                q.append((yy,xx))       
        

T=int(input())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
# visited=[False]*(n+1)


for _ in range(T):
    # n : 가로, m : 세로
    width,height,cabbage=map(int,input().split())
    field=[[0]*width for _ in range(height)]
    bug=0
    
    # 배추를 심음
    for _ in range(cabbage):
        # a : 가로, b : 세로
        w,h=map(int,input().split())
        field[h][w]=1

    for i in range(height):
        for j in range(width):
            if field[i][j]==1:
                field[i][j]-=1
                bfs(i,j)
                bug+=1
                print(bug)
    print(bug)