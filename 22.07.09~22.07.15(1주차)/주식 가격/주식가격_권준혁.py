# def solution(prices):
#     answer = []
#     for i in range(len(prices) - 1):
#         for j in range(i+1,len(prices)):
#             if prices[j] < prices[i]:
#                 answer.append(j-i)
#                 break
#         else:
#             answer.append(len(prices) - i - 1)
#     answer.append(0)
#     return answer

# 스택 풀이
def solution(prices):
    n = len(prices)
    answer = [0]*n
    stk = []
    for idx,p in enumerate(prices):
        while(stk and prices[stk[-1]] > p):
            top = stk.pop()
            answer[top] = idx - top
        else:
            stk.append(idx)
    while(stk):
        top = stk.pop()
        answer[top] = (n-1)-top
    return answer