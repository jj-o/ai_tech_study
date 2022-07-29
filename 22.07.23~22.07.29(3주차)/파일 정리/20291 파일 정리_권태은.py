import sys
import collections
input=sys.stdin.readline



def solution(num):
    global file, dict
    dict={}
    for _ in range(num):
        file=input().strip().split('.')[1]
        if file not in dict:
            dict[file]=1
        else:
            dict[file]+=1
    file=list(dict.keys())
    dict=collections.OrderedDict(sorted(dict.items()))
    return dict


num=int(input())
solution(num)

for i in dict:
    print(i,dict[i])


    