def solution(scoville, K): 
    answer = 0
    cal=0
    while(cal<K):
        answer+=1
        first=min(scoville)
        scoville.remove(min(scoville))
        second=min(scoville)
        cal=first+2*second
        scoville.append(cal)
        print(scoville)
        
        if len(scoville)==1:
            if scoville<K:
                answer=-1
    print(answer)

solution([1, 2, 3, 9, 10, 12], 7)



    
