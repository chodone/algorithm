blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_name = list(set(blood_types)) # 중복제거를 위한  - set -> 혈액형 이름 구하기

blood_types_dict = {}


for name in blood_name:
    blood_types_dict[name] =  blood_types.count(name)   # count()함수를 통한 사람 수 구하기

print(blood_types_dict)