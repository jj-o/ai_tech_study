# from functools import reduce
# def multiply(arr):
#     return reduce(lambda x, y: x * y, arr)
# def solution(clothes):
#     answer = 0
#     tmp=[]
#     dic={i[1]:[] for i in clothes}
#     for i in clothes:
#         dic[i[1]].append(i[0])
#     for key,value in dic.items():
#         tmp.append(len(value)+1)
#     return multiply(tmp)-1

from functools import reduce
from collections import Counter
def solution(clothes):
    dic = []
    for c in clothes:
        dic.append(c[1])
    dic = Counter(dic)
    return (reduce(lambda x,y:x*(y+1),dic.values(),1) - 1)