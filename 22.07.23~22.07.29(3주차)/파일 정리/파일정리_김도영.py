import sys
input = sys.stdin.readline

# 파일의 개수 N 입력
n = int(input())
file_dict = {}

for i in range(n):
    file_n = input().split('.')[1].replace('\n', '')
    if file_n not in file_dict.keys():
        file_dict[file_n] = 1
    else:
        file_dict[file_n] += 1
        
result = sorted(list(file_dict.keys()))

for i in result:
    print(i + ' ' + str(file_dict[i]))