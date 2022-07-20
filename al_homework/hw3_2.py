# 윤년 구하기

# 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년.
# 400의 배수이면 윤년
# 위 두 조건 중 하나라도 맞으면 윤년이다.

year = int(input())

if not year % 4 and year % 100:
    print('윤년입니다')
elif not year % 400:
    print('윤년입니다')
else:
    print('윤년이 아닙니다')

