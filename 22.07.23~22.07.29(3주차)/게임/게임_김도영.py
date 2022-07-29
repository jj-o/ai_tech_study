# 풀이1
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) <= z:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
            
    print(answer)
    
    
# 풀이2
x, y = map(int, input().split())
z = (y * 100) // x

def binary_search(z, start, end):
    if z >= 99:
        return -1
    result = []
    while start <= end:
        mid = (start + end) // 2
        new_z = ( (y + mid) * 100) // (x + mid)
        if new_z > z:
            result.append(mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

if binary_search(z, 1, x) == -1:
    print(-1)
else:
    print(min(binary_search(z, 1, x)))