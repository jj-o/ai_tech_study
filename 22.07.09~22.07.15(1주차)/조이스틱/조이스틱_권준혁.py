def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i,l in enumerate(name):
        answer += min(ord(l) - ord('A'),ord('Z') - ord(l) + 1)
        
        next_A = i + 1
        while next_A < len(name) and name[next_A] == 'A':
            next_A += 1
        min_move = min([min_move,2*i + len(name) - next_A, i + 2*(len(name) - next_A)])
    answer += min_move
    return answer

name = "JEROEN"

print(solution(name))