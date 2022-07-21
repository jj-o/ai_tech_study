def solution(people, limit):
    people.sort()
    lt,rt,cnt = 0,len(people) - 1,0
    while(lt <= rt):
        if (lt == rt):
            cnt += 1
            break
        elif people[lt] + people[rt] <= limit:
            lt += 1
            rt -= 1
            cnt += 1
        else:
            rt -= 1
            cnt += 1
    return cnt