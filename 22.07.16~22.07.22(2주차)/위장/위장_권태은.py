
def solution(clothes):
    closet={}
    answer=1
    
    # dictionary에 저장
    for cloth in clothes:
        # 이미 dictionary에 키 값이 있는 경우
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        # dictionary에 키 값이 없는 경우 key와 value를 저장
        else:
            # [cloth[0]] 겉에 대괄호 씌워야 함(주의)
            closet[cloth[1]]=[cloth[0]]
    
    # headgear 에 2가지가 있다면 3가지 경우가 있음
    # eyewear 에 1가지가 있어 2가지 경우
    # 3*2-1=5 (아무것도 안 입는 경우 제외)
    for value in closet.values():
        answer *= len(value)+1
        
    return answer-1