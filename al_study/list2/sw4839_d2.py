


def Tree(P, target):
    I = 1
    R = P
    cnt = 0
    while True:
        C = int((R+I)/2)

        if C < target:
            I = C
            cnt += 1
        elif C > target:
            R = C
            cnt += 1
        else:
            
            break

    return cnt


    




for tc in range(int(input())):
    P , A , B = map(int , input().split(" "))
    result = []
    
    
    if Tree(P, A) > Tree(P, B):
        result.append('B')
    elif Tree(P, A) < Tree(P, B):
        result.append('A')
    else:
        result.append(0)


    print(f'#{tc+1} {result[0]}')



