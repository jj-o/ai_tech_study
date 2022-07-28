x, y = map(int,input().strip().split())

left = 1
right = int(1e9)
win_rate = y*100//x
answer = int(1e9)

while left <= right:
    mid = (left + right)//2
    new_rate = ( y + mid ) * 100 // ( x + mid ) 

    if new_rate != win_rate:
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid+1

if answer == int(1e9):
    print(-1)
else:
    print(answer)