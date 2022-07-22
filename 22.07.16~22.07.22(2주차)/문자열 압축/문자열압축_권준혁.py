def solution(s):
    answer = 10**7
    units = [i for i in range(1,len(s)//2 + 1)]+[len(s)]
    for u in units:
        words = [s[i:i+u] for i in range(0,len(s),u)]
        res,cur_word,cur_cnt = '',words[0],1
        for w in words[1:]+['']:
            if cur_word == w:
                cur_cnt += 1
            else:
                res += (('' if cur_cnt == 1 else str(cur_cnt)) + cur_word)
                cur_word = w
                cur_cnt = 1
        answer = min(answer,len(res))
    return answer