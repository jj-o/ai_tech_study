# 전체 사람의 수 N 입력
n = int(input())
w_h = []

# N명의 몸무게와 키 받기
for i in range(n):
    w_h.append(list(map(int, input().split())))
    
# N명의 덩치 등수 출력
for i in range(n):
    print(len([a for a in w_h if (a[0] > w_h[i][0]) and (a[1] > w_h[i][1])]) + 1, end= ' ')