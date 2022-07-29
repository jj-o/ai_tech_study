import sys
input=sys.stdin.readline



def solution():
    global file, dict, num
    dict={}
    num=int(input())
    for _ in range(num):
        file=input().strip().split('.')[1]
        if file not in dict:
            dict[file]=1
        else:
            dict[file]+=1
    file=list(dict.keys())
    file=file.sort()
    return file


solution()      
for i in file:
    print(i,dict[i])


    