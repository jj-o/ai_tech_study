def solution(s):
    length=[]
    result=""

    for piece in range(1,len(s)//2+1):
        cnt=1
        temp=s[:piece]
        
        for i in range(piece, len(s), piece):
            if s[i:i+piece]==temp:
                print(s[i])
                print(s[i+piece])
                cnt +=1
            else:
                if cnt==1:
                    cnt=""
                result += str(cnt)+temp
                temp=s[i:i+piece]
                cnt=1
        
        if cnt==1:
            cnt=""
        result += str(cnt)+temp
        length.append(len(result))
        result=""
    print(min(length))  

solution("ababcdcdababcdcd")

    