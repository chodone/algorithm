
# 색칠하기

# 입력받은 5개의 값들을 list화 해서 [-1] 인덱스로 색 구별
# 앞에 4개의 숫자들 가지고 이중 for문을 통해 좌표 리스트 구성
# 튜플 교집합을 통해 purple 개수 구하기




for tc in range(int(input())):
    N = int(input())

    red_lst= []
    blue_lst = []

    # 이중 for문을 통한 좌표구하기
    for _ in range(N):
        check_lst = list(map(int , input().split(" ")))
        if check_lst[-1] == 1:
            for i in range(check_lst[0] , check_lst[2]+1):
                for j in range(check_lst[1] , check_lst[3]+1):
                    red_lst.append((i,j))
        else:
            for i in range(check_lst[0] , check_lst[2]+1):
                for j in range(check_lst[1] , check_lst[3]+1):
                    blue_lst.append((i,j))

    # set 교집합을 통한 purple 개수 구하기
    purple = set(red_lst) & set(blue_lst)
    result = len(purple)

    print(f'#{tc+1} {result}')






