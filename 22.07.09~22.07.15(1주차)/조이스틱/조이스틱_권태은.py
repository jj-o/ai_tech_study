# 만들고자 하는 이름이 매개변수, 조이스틱 조작 횟수의 최솟값
def solution(name):
    s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 0
    for a in name:
        if s.index(a)>13:
            answer+=26-s.index(a)
        else: 
            answer+=s.index(a)
            
    b=len(name)-1
    answer+=b
    
    for i in range(1,len(name)//2+1):
        if name[i]=='A' and name[-1*i]!='A':
            answer-=b
            answer+=i
            print(answer)
        else:
            answer-=b
            answer+=len(name)-1
            print(answer)
    
    return answer

# hidden case에서 안 되는 경우가 있음