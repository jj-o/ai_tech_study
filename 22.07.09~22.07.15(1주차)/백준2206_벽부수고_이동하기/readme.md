# 벽을 한 개 뿌셔서 왼쪽 위부터 오른쪽 아래로 감.
# dfs가 아닌 bfs를 사용하는 이유 : dfs는 한 길 끝까지 간 다음 길을 가기 때문에 수행시간 면에서 비효율. bfs는 모든 경우의 수를 한 걸음 씩 감 (시간복잡도가 낮음)
from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
visited = [[[0]*2 for _  in range(col)] for _ in range(row)]
dir = [[-1,0],[1,0],[0,-1],[0,1]] # 좌 우 하 상

def bfs():
    q=deque([(0,0,0)])
    visited[0][0][0]=1
    graph=[]

    while q:
        r,c,wall=q.popleft()
        if r==row-1 and c==col-1:
            
            
            
            # r행 c열까지 벽을 wall개 부수고 이동하는 최단거리 ( 이 문제에서는 벽을 하나만 부술 수 있음 )
            return visited[r][c][wall]

        for i in range(4):
            nr=r+dir[i][0]
            nc=c+dir[i][1]
            # 맵 범위 안에 있고, 한 번도 방문하지 않았으면
            if 0<=nr<row and 0<=nc<col and visited[nr][nc][wall]==0:
                # 벽이 아니라면 이동하고, 이전경로+1 visited 배열에 저장
                if graph[nr][nc]==0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall]=visited[r][c][wall]+1

                if wall==0 and graph[nr][nc]==1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로+1 저장
                    visited[nr][nc][1]=visited[r][c][wall]+1
    return -1
