import heapq as hq
def solution(scoville, k):
    answer = 0
    hq.heapify(scoville)
    while(1):
        first = hq.heappop(scoville)
        if first >= k:
            return answer
        elif first < k:
            if len(scoville) == 0:
                return -1
            else:
                answer += 1
                hq.heappush(scoville,first + hq.heappop(scoville) * 2)