

case=int(input())
ans=[]
for i in range(case):
    answer=[]
    xx=[0]
    yy=[0]
    spots=int(input())
    for j in range(spots):
        x,y=list(map(int,input().split()))
        xx.append(x)
        yy.append(y)
        answer.append(abs(xx[j+1]-xx[j])+abs(yy[j+1]-yy[j]))
    answer.append(abs(xx[len(xx)-1])+abs(yy[len(yy)-1]))
    ans.append(sum(answer))

for i in range(len(ans)):
    print(ans[i])
    