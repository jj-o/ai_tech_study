import sys
input = sys.stdin.readline

n = int(input().strip())
dic = {}
for _ in range(n):
    f = (input().strip()).split('.')
    try:
        dic[f[1]] += 1
    except:
        dic[f[1]] = 1
dic = sorted(dic.items(),key=lambda x:x[0])
for d in dic:
    print(f'{d[0]} {d[1]}')