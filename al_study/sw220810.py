import sys
sys.stdin = open("input.txt", "r")






TC = 10

for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int , input().split())) for _ in range(100)]

    totalSum = []
    # 가로합
    for row in range(100):
        rowSum = 0
        for column in range(100):
            rowSum += arr[row][column]
        totalSum.append(rowSum)

    


        
    # 세로합
    for column in range(100):
        columnSum = 0
        for row in range(100):
            columnSum += arr[row][column]
        totalSum.append(columnSum)
    

    
    #정방향 대각선 합
    diagSum = 0
    for idx in range(100):
        diagSum += arr[idx][idx]
    totalSum.append(diagSum)

    

    #역방향 대각선 합
    revDiagSum = 0
    for idx in range(99,-1,-1):
        revDiagSum += arr[idx][idx]
    totalSum.append(revDiagSum)

    
    
    #최대값 구하기
    maxSum = totalSum[0]
    for num in totalSum[1:]:
        if num > maxSum:
            maxSum = num 

    print(f'#{tc} {maxSum}')

   
    




            



    

