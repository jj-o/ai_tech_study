# def check_row(row:int,col:int) -> bool:
#     global board
#     for i in range(col):
#         if i != col:
#             if board[i] == row:
#                 return False
#     return True

# def check_diagonal(row:int,col:int) -> bool:
#     global board
#     for i in range(col):
#         if abs(board[col] - board[i]) == col - i:
#             return False
#     return True

# def dfs(level:int):
#     global board,answer,num
#     if level == num:
#         answer += 1
#     else:
#         for i in range(num):
#             board[level] = i
#             if check_row(board[level],level) and check_diagonal(board[level],level):
#                 dfs(level + 1)
                     
# def solution(n):
#     global board,answer,num
#     num = n
#     answer = 0
#     board = [0] * n
#     dfs(0)
#     return answer

# 퀸은 row+col이 같은 칸과 row-col이 같은 칸을 공격할 수 있습니다.
# n = 3일 때, (2, 2)에 있는 퀸은 (1, 3), (3, 1), (1, 1), (3, 3) 등을 공격할 수 있습니다.
def dfs(row:int) -> int:
    global check_col,check_diagonal1,check_diagonal2,num
    result = 0
    if row == num+1:
        return 1
    # row 에서의 다음 col 선택
    for col in range(1,num+1):
        d1 = row + col
        d2 = num + (row - col)
        # 특정한 (row,col)에 퀸을 뒀을 때, 퀸이 공격할 수 있는 칸을 사전에 True로 표시해서
        # dfs(row + 1)로 다음 row에서의 col을 선택할 때,
        # 공격이 가능한 칸은 무시할 수 있도록 한다.
        if (check_col[col] == False) and (check_diagonal1[d1] == False) and (check_diagonal2[d2] == False):
            check_col[col] = True
            check_diagonal1[d1] = True
            check_diagonal2[d2] = True
            result += dfs(row + 1)
            check_col[col] = False
            check_diagonal1[d1] = False
            check_diagonal2[d2] = False
        # 공격이 가능한 칸이 있으므로, 무시
        else:
            continue
    return result

def solution(n):
    global check_col,check_diagonal1,check_diagonal2,num
    num = n
    check_col = [False] * 100
    check_diagonal1 = [False] * 100
    check_diagonal2 = [False] * 100
    return dfs(1)