import sys
input = sys.stdin.readline

# 입력
x,y = map(int,input().split())

# 솔루션 함수
def solution(x,y):
    answer = 0
    z = y * 100 // x
    if z >= 99:
        return -1
    lt = 1
    rt = x
    while(lt <= rt):
        mid = (lt + rt) // 2
        if ((y+mid) * 100 // (x+mid) ) <= z:
            lt = mid + 1
        else:
            answer = mid
            rt = mid - 1
    return answer

print(solution(x,y))