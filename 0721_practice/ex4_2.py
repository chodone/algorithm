


students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

# students 중복된 이름 없애서 이름 구하기
students_name = list(set(students))
print(students_name)


# 이름과 득표수 딕셔너리 만들기
students_dict = {}
for name in students_name:
    
    count = 0
    for count_name in students:  
        if count_name == name:
            count += 1
    students_dict[name] = count

print(sorted(students_dict.items() , key= lambda x:x[1] ,reverse = True) )
    
# sorted() 복습...
# key= 무엇을 기준으로 정렬할 것인가를 결정

# lambda는 간단한 함수를 표현 lambda 파라미터 : 함수식
# 표현식을 계산한 결과값을 반환하는 함수
