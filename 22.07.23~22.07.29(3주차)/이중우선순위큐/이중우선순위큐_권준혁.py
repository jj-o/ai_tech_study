def solution(operations):
    q = []
    for o in operations:
        op = o.split()
        if op[0] == 'I':
            tmp = int(op[1])
            q.append(tmp)
            q.sort()
        elif op[0] == 'D':
            if q:
                if op[1] == '-1':
                        q.pop(0)
                else:
                    q.pop()
    if q:
        if len(q) == 1:
            return q.pop()
        else:
            tmp = q.pop()
            return [tmp,q.pop(0)]
    else:
        return [0,0]