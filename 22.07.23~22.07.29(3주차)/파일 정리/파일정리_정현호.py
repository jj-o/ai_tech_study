import sys

answer = {}

n = int(input())
for _ in range(n):
    k = sys.stdin.readline().strip().split('.',1)
    answer[k[1]]=answer.get(k[1],0)+1

for i,j in sorted(answer.items(), key=lambda x:x[0]):
    print(i,j)