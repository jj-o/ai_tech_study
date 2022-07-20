import sys
input = sys.stdin.readline

# 입력값 지정
n = int(input().strip())
info = [list(map(int,input().split())) for _ in range(n)]
# solution 함수
def solution(n:int,info:list)->list:
    answer = []
    for i in range(n):
        cnt = 1
        for j in range(n):
            if i != j and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                cnt += 1
        answer.append(cnt)
    return answer
print(*solution(n,info))