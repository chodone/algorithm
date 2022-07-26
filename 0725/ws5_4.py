def sum_of_repeat_number(numList):
    result = []
    for num in numList:
        if numList.count(num) == 1:   # count() 함수의 사용 - 인자가 몇개있는지 값 반환
            result.append(num)
    
    return sum(result)

            



sample = [4, 4, 7,  8, 10, 4]
print(sum_of_repeat_number(sample))

