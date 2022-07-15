import heapq

# 힙 정렬
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)  

    return [heapq.heappop(h) for i in range(len(iterable))]


def solution(scoville, K):

    scoville = heapsort(scoville)
    cnt = 0

    while scoville:
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return cnt
        else:
            if not scoville:
                return -1
            else:                
                min_2 = heapq.heappop(scoville)
                new_v = min_1 + (min_2 * 2)
                heapq.heappush(scoville, new_v)
                cnt += 1
