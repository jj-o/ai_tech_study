import heapq


def solution(operations):
    priority=[]
    result=[]
    for word in operations:
        sign,num=word.split(" ")
        print(sign)
        num=int(num)
        if sign=='I':
            heapq.heappush(priority,num)
        elif sign=='D':
            if num>0:
                priority.pop(priority.index(heapq.nlargest(1,priority)[0]))
            else:
                # heapify하면 힙 구조에 맞추어 재배치, 0번째 인덱스에 위치
                heapq.heapify(priority)
                heapq.heappop(priority)
    if priority:
        result=[max(priority),min(priority)]
    else:
        result=[0,0]
    return result

print(solution(operations))