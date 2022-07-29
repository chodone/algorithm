tc = int(input())

margin_lst = []

max_price = 0

for _ in range(tc):
    N = int(input())
    price_lst = list(map(int , input().split(" ")))
     
    margin = 0
    
    while True:
        max_price = sorted(price_lst)[-1]

        price_lst.index(max_price)

        for price in price_lst[:price_lst.index(max_price)]:
            margin += (max_price - price)
        
        price_lst = price_lst[price_lst.index(max_price) + 1:]
        
        if not price_lst:
            break
    
    margin_lst.append(margin)

idx = 1
for margin in margin_lst:

    print(f'#{idx} {margin}')
    idx += 1

'''
3일동안 매달린 백만장자 문제...

1. 문제를 파악할때 아이디어를 잘못 접근했다 -> 처음 생각했던 알고리즘 = 인덱스의 증가 감소를 판단하여 max price를 결정하고 그 앞에 인덱스 값들을 빼주기
2. 두번째 생각한 알고리즘 - 리스트를 순회하면서 max price를 결정하고 그 앞에 인덱스 값들을 빼준다 -> 런타임 에러가 발생한다. 생각해보면 리스트의 데이터가 100개가 넘어간다면 계속 for문을 통해 max_price를 구하므로 시간이 오래걸릴 수 밖에 없다
3. 세번째 생각한 알고리즘 - sorted()함수를 통해 max price를 결정하고 리스트의 그 인덱스 값을 구한 후 for문을 돌린다. 그 뒤에 계산이 끝난 인덱스들은 슬라이싱을 통해 잘라내고 새로운 리스트를 출력, 그 다음에 다시 for문을 돌린다.

'''


    



    
        




