people=int(input())
body=[list(map(int,input().split())) for _ in range(people)]
rank=[1 for _ in range(people)]

def solution():
    global rank
    for i in range(people):
        for j in range(people):
            if body[i][0]<body[j][0] and body[i][1]<body[j][1] :
                rank[i]+=1
    return rank 

solution()
for i in rank:
    print(i,end=" ")
    
    
    


