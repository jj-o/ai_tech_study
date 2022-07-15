def solution(numbers, target):
    root=[0]
    for i in numbers:
        b=[]
        for j in root:
            b.append(j+i)
            b.append(j-i)
        root=b
    return root.count(target)