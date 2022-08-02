





for tc in range(int(input())):
    
    K, N, M = map(int, input().split(" "))
    start = 0

    #정류장 , 충전소 리스트 만들기 
    stop_lst = [False] * (N+1)
    charge_lst = list(map(int , input().split(" ")))
    stop_lst[0] = True

    #정류장 충전소 True 만들기

    for charge in charge_lst:
        stop_lst[charge] = True

    
    
    newStop_lst = stop_lst[::K]
    idx = 0
    result = 0
    for chargeStop in newStop_lst:
        
        if chargeStop:
            result += 1
            continue
        else:
            for newChargeStop in stop_lst[idx:idx-K:-1]:
                if newChargeStop:
                    newStop_lst = stop_lst[idx::K]
                    idx -= 1
                    result += 1 
                    break
                else:
                    result = 0 

        idx += K

    print(f'#{tc+1} {result}')

    
