from unittest import result


t = int(input())

result_lst = []


for i in range(t):
    result = 0
    n = int(input())
    for j in range(1,n+1):

        if not j % 2:
            result -= j
        else:
            result += j

    result_lst.append(result)

for i in range(t):
    print(f'#{i+1} {result_lst[i]}')
        


