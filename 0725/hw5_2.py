def leap_year(year):
    pass
    if (not year % 4 and year % 100) or not year % 400:  
        message_str = f'{year}년은 윤년입니다'
        return message_str
    else:
        message_str = f'{year}년은 윤년이 아닙니다'
        return message_str

print(leap_year(2021))
print(leap_year(2020))
