caseNum = int(input())


case_margin_lst = []

for i in range(caseNum):
    margin_lst = []
    max_price = 0
    margin = 0
    increase = True
    n = int(input())
    if 2 <= n <= 1000000:
        pass   
        case_lst = list(map(int , input().split()))
        if len(case_lst) != n:
            print("잘못된입력")
        else:
            while increase:
                for case in case_lst:
                    margin_lst.append(case)
                    max_price = case
                if case < max_price:
                    for mar in margin_lst:
                        margin += (max_price-mar)


        
        

    
    else:
        print("잘못된 입력")

for i in range(caseNum):
    print(f'#{i+1} {case_margin_lst[i]}')


