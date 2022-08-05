
for tc in range(int(input())):
    str1 = tuple(input())
    str2 = list(input())

    result_dict = {}

    for alp in str1:
        cnt = 0
        cnt += str2.count(alp)

        result_dict[alp] = cnt

    print(f'#{tc+1} {max(result_dict.values())}')
