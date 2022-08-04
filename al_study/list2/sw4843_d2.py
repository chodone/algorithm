

for tc in range(int(input())):
    N = int(input())

    minNum_lst = []
    maxNum_lst = []


    if not N % 2:
        check_lst = list(map(int , input().split(" ")))
        check_lst.sort()
        minNum_lst = check_lst[:N/2]
        maxNum_lst = check_lst[N/2:]

        


    else:
        check_lst = list(map(int , input().split(" ")))
        check_lst.sort()
        minNum_lst = check_lst[:N//2]
        maxNum_lst = check_lst[N//2:]



    


