


fruits = 'apple,rottenBanana,apple,RoTTenorange,Orange'

# 함수 사용해서 만들어보기
fruits_list = list(fruits.split(','))     # 문자열이 ','로 나누어져 있으므로 split(',') 함수를 통해 리스트 형태로 만들기


newFruits_list = []
for fruit in fruits_list:
    lowerfruit = fruit.lower()  # 소문자로 바꾸는 메서드 .lower() - lower()함수는 원본을 건드리지 않고 새로운 문자열을 생성한다
    if lowerfruit[:6] == 'rotten':
        newFruits_list.append(lowerfruit[6:])  # 슬라이싱[] - 얕은복사: 원본에 영향을 주지 않는다.
        
    else:
        newFruits_list.append(lowerfruit)
    
    
print(newFruits_list)


# for 문을 도는 literable 리스트의 값을 insert() 함수로 변환시켰기에 무한루프가 돌았다

'''

fruit = fruit.lower()
fruit = fruit.replace('rotten', '')
fruitLst = fruit.split(',')
print(fruitLst)

'''