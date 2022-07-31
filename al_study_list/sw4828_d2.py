# min_max




testCase = int(input())

for tc in range(testCase):
    N = int(input())
    
    numList = list(map(int , input().split()))

    numList.sort()

    result = numList[-1] - numList[0]

    print(f'#{tc+1} {result}')


