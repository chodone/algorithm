# 문자열 비교


for tc in range(int(input())):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{tc+1} 1')

    else:
        print(f'#{tc+1} 0')

    