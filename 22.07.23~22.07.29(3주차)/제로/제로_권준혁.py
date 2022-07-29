import sys
input = sys.stdin.readline

n = int(input().strip())
stk = []
for _ in range(n):
    tmp = int(input().strip())
    if tmp == 0:
        stk.pop()
    else:
        stk.append(tmp)
print(sum(stk))