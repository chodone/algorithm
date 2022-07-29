


testcase = int(input())

for tc in range(testcase):

    N = int(input())
    if 2 <= N <= 30:
        distan = 0
        now_vel = 0
        for _ in range(N):
            

            command = list(map(int , input().split(" ")))
            com = command[0]
            
            if len(command) == 2:
                vel = command[1]
            
            
            if vel != 1 and vel != 2:
                print('가속도를 잘못입력하였습니다')
                break
            elif com != 0 and com != 1 and com != 2:
                print("잘못된 command를 입력하였습니다.")
                break
            else:
                if com == 1:
                    now_vel += vel
                    distan += now_vel 
                elif com == 2:
                    if now_vel:
                        now_vel -= vel
                        distan += now_vel 
                    else:
                        continue
                elif com == 0:
                    distan += now_vel

    
    else:
        print('잘못된 입력')
        break
    print(f'#{tc+1} {distan}')