def solution(board, moves):
    answer = 0
    stk = []
    l = len(board[0])
    for loc in moves:
        # 0~n까지 행 탐색
        for idx in range(l):
            tmp = board[idx][loc-1]
            if tmp != 0:
                board[idx][loc-1] = 0
                if len(stk) != 0:
                    if stk[-1] == tmp:
                        stk.pop()
                        answer+=2
                    else:
                        stk.append(tmp)
                else:
                    stk.append(tmp)
                break
    return answer