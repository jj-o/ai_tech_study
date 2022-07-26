def solution(genres, plays):
    answer = []
    dic = {}
    for idx,(g,p) in enumerate(zip(genres,plays)):
        try:
            tmp = dic[g][-1][2]
            dic[g].append([p,idx,tmp + p])
        except:
            dic[g] = [[p,idx,p]]
    dic = sorted(dic.items(),key=lambda x:(-x[1][-1][2]))
    for i in range(len(dic)):
        dic[i] = list(dic[i])
        for j in range(len(dic[i][1])):
            dic[i][1] = sorted(dic[i][1],key=lambda x:(-x[0],x[1]))
    for i in range(len(dic)):
        cnt = 0
        for j in range(len(dic[i][1])):
            if cnt == 2:
                break
            answer.append(dic[i][1][j][1])
            cnt += 1
    return answer