

for T in range(int(input())):
    n = int(input())
    qList = []
    for i in range(n):
        minList=list(input().split())
        qList.append(minList)

    resultList = []
    minList=[]
    for i in range(n):
        ans=''
        for k in range(1,n+1): 
            ans += qList[n-k][i]
        minList.append(ans)

    resultList.append(minList)

    minList=[]
    for i in range(n-1,-1,-1):
        ans2=''
        for j in range(1,n+1):
            ans2 += qList[i][n-j]
        minList.append(ans2)

    resultList.append(minList)

    minList=[]
    for i in range(n-1,-1,-1):
        ans3=''
        for j in range(n):
            ans3 += qList[j][i]
        minList.append(ans3)
 
    resultList.append(minList)
 
    print(f'#{T+1}')
    result=''
    for i in range(n):
        for j in range(3): 
            result+=resultList[j][i]
            result += ' '
        result += '\n'

    result=result[:len(result)-2]
    print(result)



