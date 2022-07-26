# 반복문을 사용X
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


print(sum_of_digit(input()))
print(sum_of_digit_for(input()))