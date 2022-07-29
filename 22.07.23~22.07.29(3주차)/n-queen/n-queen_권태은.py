from itertools import count
import sys
from collections import deque
input=sys.stdin.readline

def dfs(v):
    print(v,end=" ")
    visited[v]=True
    
    for i in range(1,n+1):
        if visited[i]==False and graph[v][i]==1:
            dfs(i)
        print(visited)
    
def dfs(depth):
    global count
    if depth == n:
        count +=1
        return
    
    for i in range(n):
        if visited[i]==0:
            graph[depth]=i
            
            t=True
            for j in range(depth):
                # 대각선
                if abs(graph[depth]-graph[j])==abs(depth-j):
                    t=False
                    break
                if abs(graph[depth]+graph[j])==abs(depth+j):
                    t=False
                    break
            if t:
                print(graph,depth)
                visited[i]=1
                dfs(depth+1)
                visited[i]=0
                
n=int(input())

graph=[0]*n
visited=[0]*n

count=0
dfs(0)