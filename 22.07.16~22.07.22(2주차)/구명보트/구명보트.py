
def solution(people, limit):
    people.sort()
    ans=0
    l = 0
    h = len(people)-1
    
    while (l<h):
        if people[l]+people[h]<=limit:
            ans +=1
            l+=1
            h-=1
        else:
            h-=1
            ans+=1
    if l==h:
        ans+=1
    
    return ans

print(solution([70,50,80,50],100))

