def solution(citations):
    answer=0
    citations=sorted(citations)
    for i in citations:
        idx=citations.index(i)
        if len(citations[idx:])>=i and len(citations[:idx])<=i:
            h=i
    if h==0:
        return len(citations)
    return answer

# 4 4 4 => 3 반례