# 반복문을 사용X
from unittest import result


def sum_of_digit(num):
    num_list = list(num)
    intNum_list = list(map(int , num_list))
    
    return sum(intNum_list)

# 반복문 사용 O
def sum_of_digit_for(num):
    result = 0
    for digit in num:
        result += int(digit)
    return result

# 재귀 사용
def sum_of_digit_r(n):
    if n < 10:
       return n
    else:
        t = sum_of_digit_r(n//10) + (n%10)
        return t
    
    

result = sum_of_digit_r(2456)
print(result)

# print(sum_of_digit(input()))
# print(sum_of_digit_for(input()))