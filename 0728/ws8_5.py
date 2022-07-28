def hanoi(N, start, to, via):
    if N == 1:
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮깁니다.".format( start, N , to))
    else:
        hanoi(N-1, start, via, to)       
        print("{}번 기둥의 {}번 원반을 {}번 기둥에 옮깁니다.".format( start, N , to))
        hanoi(N-1, via, to, start)
                
        
        


hanoi(3, 'A', 'C', 'B')


# A번 기둥의 1번 원반을 C번 기둥에 옮긴다.
# A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
# C번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 A번 기둥에 옮긴다.
# B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
# A번 기둥의 1번 원반을 C번 기둥에 옮긴다.