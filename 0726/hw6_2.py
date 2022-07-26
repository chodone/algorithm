
salt = 0
saltwater = 0


while True:
    # 함수를 통한 불필요한 단위 제거
    s = input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:")
    if s != 'Done':
        newS = list(map(str , s.split(" ")))
        salt += (float(newS[0][:1]) * float(newS[1][:3])) / 100
        saltwater += float(newS[1][:3])


    else:
        break


density = salt/saltwater * 100

print(f'{round(density, 2)}% {round(saltwater, 2)}g')