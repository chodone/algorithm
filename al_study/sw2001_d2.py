for testcase in range(1, int(input())+1):
    result = 0
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
   
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            check = 0
            
            for a in range(i, i+m):
                for b in range(j, j+m):
                    check += maps[a][b]

            answer = max(answer, check)
    print(f'#{testcase}', result)


