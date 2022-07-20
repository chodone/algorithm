orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

# 메뉴 개수 구하기
new_orders = orders.split(",")
ordersNum = 0

for i in new_orders:
    ordersNum += 1 
print(ordersNum)

# 메뉴 중복 제거 후 내림차순 형태 리스트로 표현
nonOverlapOrder = set(new_orders)
nonOverlapOrder = sorted(list(nonOverlapOrder) , reverse = True)
print(nonOverlapOrder)


# split() 함수는 list형태로 반환해준다
# set을 통한 중복 제거

# sorted() 와 list.sort()의 차이

# sorted()
# 새로운 리스트를 생성 후 반환한다. 기존의 리스트의 손실 없음 
# key 매개변수를 통해 정렬하기 전 각 요소에 대하여 적용되는 함수를 지정 가능
# reverse = True를 통해 내림차순 - 기본이 오름차순으로 정렬

# list.sort()
# 기존의 리스트를 오름차순으로 정렬시킨다. 기존 리스트 데이터 변환
# reverse = True를 통헤 내림차순


