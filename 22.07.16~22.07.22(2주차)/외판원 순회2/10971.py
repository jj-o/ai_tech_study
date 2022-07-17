import sys

city=int(input())
# tot_cost[i][j] i에서 j로 가기 위한 비용
tot_cost=[list(map(int, input().split())) for _ in range(city)]
visited=[]
min_cost = sys.maxsize

def dfs_backtracking(start, next, cost, visited):
    if len(visited)==city: # 도시들 한 번 씩 돌고 마지막 도시에서 처음 도시로 가는 경우
        if tot_cost[next][start]!=0:
            min_cost=min(min_cost, cost+tot_cost[next][start])
        return

    for i in range(city):
        # 모든 도시를 도는데 드는 비용의 현재 최소값보다 크면 계산할 필요가 없다. (최솟값 계산이니까)
        if tot_cost[next][i]!=0 and i not in visited and cost<min_cost:
            visited.append(i)
            dfs_backtracking(start, i, cost+tot_cost[next][i], visited)
            visited.pop()
            

# visited 리스트에 넣어서 도시마다 출발지점 지정
for i in range(city):
    if tot_cost[0][i]:
        dfs_backtracking(i,i,0,[i])
        
print(min_cost)