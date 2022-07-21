def solution(clothes):
    hash_map = {}
    for clothe in clothes:
        hash_map[clothe[1]] = hash_map.get(clothe[1], 0) + 1
        
    answer = 1
    for i in hash_map:   
        answer *= (hash_map[i] + 1)
    
    return answer - 1