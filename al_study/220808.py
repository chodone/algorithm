def getValue(pos, BLD):
    near_lst = [BLD[pos-2], BLD[pos-1], BLD[pos+1], BLD[pos+2]]

    maxHeight = 0

    for height in near_lst:
        if maxHeight < height:
            maxHeight = height
    
    if BLD[pos] > maxHeight:
        return BLD[pos] - maxHeight
    else:
        return 0




TC = 10

for tc in range(1, TC+1):
    N = int(input())

    BLD = list(map(int , input().split()))

    sumV = 0
    for i in range(2, N-2):
        t = getValue(i, BLD)
        sumV += t

    print(f'#{tc} {sumV}')


