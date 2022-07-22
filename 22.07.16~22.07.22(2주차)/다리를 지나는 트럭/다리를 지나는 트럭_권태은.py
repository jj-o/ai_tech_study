 # 다리를 건너는 것에 소요되는 시간

# deque 를 쓰면 테스트 케이스5에서 시간 초과 -> 클래스
def solution(bridge_length, weight, truck_weights):
    sec = 0
    sum_bridge=0
    bridge=[0 for _ in range(bridge_length)]
    
    while bridge:
        sec+=1
        a=bridge.pop(0)
        sum_bridge-=a
        
        if truck_weights:
            # brige 위에 있는 무게+들어올 기차 무게가 limit 값보다 작으면 기차가 다리 위에 올라옴.
            if sum(bridge)+truck_weights[0]<=weight:
                # truck_weigths 에서 맨 앞 값을 pop
                t=truck_weights.pop(0)
                bridge.append(t)
                sum_bridge+=t
            else:
                bridge.append(0)
        
        if len(truck_weights)==0 and sum_bridge==0:
            break
    return sec

