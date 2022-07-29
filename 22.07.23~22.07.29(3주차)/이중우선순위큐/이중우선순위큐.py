from collections import deque
operations=[["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]]

def solution(operations):
    answer=[]
    q=[]
    for word in operations:
        if word[0][0][q]=='I':
            q.append(word[1])
        else:
            if word[0][2]<0:
                q.pop(min(q))
            else:
                q.pop(max(q))
            print(q)
    answer=[max(q),min(q)]
    return answer

print(solution(operations))