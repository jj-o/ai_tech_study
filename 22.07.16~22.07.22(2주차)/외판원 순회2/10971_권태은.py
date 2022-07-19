# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로
city=int(input())
# tot_cost[i][j] i에서 j로 가기 위한 비용

cost=[list(map(int, input().split())) for _ in range(city)]
#sys.maxsize는 저장할 수 있는 가장 큰 값을 불러온 것
min_cost=1e10

def dfs_backtracking(start, cur, tot_cost, visited):
    # min_cost를 전역변수로 하여 함수 밖에서도 사용하게 하기 위함 (ex.print(min_cost))
    global min_cost
    
    if len(visited)==city: # 도시들 한 번 씩 돌고 마지막 도시에서 처음 도시로 가는 경우
        if cost[cur][start]!=0:
            #저장된 min_cost 값과 이번 경로로 계산된 값 중 작은 것을 min_cost로 함
            min_cost=min(min_cost, tot_cost+cost[cur][start])
        return

    for i in range(city):
        # cur 도시에서 i도시로 갈 수 있고, i도시는 방문하지 않았던 도시이며, 저장된 min_cost 값보다 비용이 덜 들면
        if cost[cur][i]!=0 and i not in visited and tot_cost<min_cost:
            # 그 도시를 방문목록에 추가
            visited.append(i)
            dfs_backtracking(start, i, tot_cost+cost[cur][i], visited) # 그 도시를 방문
            visited.pop() # 방문을 완료했다면 방문목록 해제
            

# visited 리스트에 넣어서 도시마다 출발지점 지정
for i in range(city):
    if cost[0][i]:
        dfs_backtracking(i,i,0,[i])
        
print(min_cost)