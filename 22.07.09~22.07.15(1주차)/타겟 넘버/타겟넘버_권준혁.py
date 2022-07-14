def dfs(numbers,level,target,res):
    global answer
    if level == len(numbers):
        if res == target:
            answer += 1
            return
        else:
            return
    else:
        dfs(numbers,level+1,target,res + numbers[level])
        dfs(numbers,level+1,target,res - numbers[level])

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers,0,target,0)
    return answer