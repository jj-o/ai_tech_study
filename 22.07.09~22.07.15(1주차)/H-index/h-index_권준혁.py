# def solution(cit):
#     answer = 0
#     cit.sort()
#     for h in range(max(cit)):
#         rt,lt = 0,0
#         for i,c in enumerate(cit):
#             if c>=h:
#                 lt = i
#                 rt = len(cit) - i
#                 break
#         if rt >= h and lt <= h:
#             answer = max(answer,h)
#     return answer

def solution(cit):
    cit.sort()
    l = len(cit)
    for i in range(l):
        if cit[i] >= l - i:
            return l - i
    return 0