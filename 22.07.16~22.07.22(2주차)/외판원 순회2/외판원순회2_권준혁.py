import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(loc,level,cost,start):
    global visited,answer
    if level == n-1:
        if city[loc][start] != 0:
            answer = min(answer,cost+city[loc][start])
        return
    else:
        for i in range(n):
            if visited[i] == False and city[loc][i] != 0:
                visited[i] = True
                dfs(i,level + 1, cost + city[loc][i],start)
                visited[i] = False

# 입력값 지정
n = int(input().strip())
city = [list(map(int,input().split())) for _ in range(n)]
# solution 함수
def solution(n,city)->int:
    global visited,answer
    answer = sys.maxsize
    visited = [False]*n
    for i in range(n):
        visited[i] = True
        # 현재위치,레벨,코스트,출발점
        dfs(i,0,0,i)
        visited[i] = False
    return answer

print(solution(n,city))