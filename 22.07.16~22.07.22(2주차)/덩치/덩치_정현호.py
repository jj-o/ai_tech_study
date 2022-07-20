import sys

n = int(input())
list_n = list(list(map(int,sys.stdin.readline().strip().split())) for i in range(n))

for i in list_n:
    rank = 1
    for j in list_n:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank,end=' ')
