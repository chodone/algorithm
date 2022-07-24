orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'


# orders를 list 형태로 반환하기
list_order = list(orders.split(","))


# for문을 통한 아이스 메뉴 파악

cnt = 0
for menu in list_order:
    if menu[:3] == '아이스':
        cnt += 1

print(f'아이스 메뉴는 {cnt}개 입니다.')


# 메뉴별 주문수 구하기

# set을 통한 메뉴 리스트 출력
menu_list = list(set(list_order))


# for문을 통한 메뉴별 주문 수 확인
for menu in menu_list:
    cnt = 0
    for order in list_order:
        if menu == order:
            cnt += 1
    print(f'{menu} : {cnt}개')





