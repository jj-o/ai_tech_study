# 정수 K 입력
k = int(input())
v_l = []

for i in range(k):
    v = int(input())
    if v == 0:
        v_l.pop()
        continue
    else:
        v_l.append(v)
try:
    print(sum(v_l))
except:
    print(0)
    
a = []
print(sum(a))