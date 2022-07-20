def solution(board, moves):
    answer = 0
    save = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                save.append(board[j][i-1])
                board[j][i-1]=0
                if len(save)>1:
                    if save[-2]==save[-1]:
                        del save[-2::1]
                        answer+=2
                        print(answer)
                break
    return answer