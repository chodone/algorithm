import random
from tkinter.messagebox import RETRY

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수
    print(answer)

    # 여기부터 코드를 작성하세요.
    while True:
        inputStr = input("1이상 10000이하의 숫자를 입력하세요:")
        counts += 1

        if not inputStr.isdecimal() or int(inputStr) < 1 or int(inputStr) > 10000:
            print("잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.")
            continue
        elif int(inputStr) < answer:
            print("up!")
            continue
        elif int(inputStr) > answer:
            print("down!")
            continue
        
        #else: if num == answer

        print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다')
        break
    '''
    while True:

        retry = input("게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요: ")

        if retry == 'y':
            break
        elif retry == 'n':
            print("이용해주셔서 감사합니다. 게임을 종료합니다")
            is_playing = False
            break

    
    
    '''    
    
    
    retry = ' '
    while not retry in ('y' , 'n'):
        retry = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요:')
        if retry == 'n':
            print('이용해주셔서 감사합니다. 게임을 종료합니다.')
            is_playing = False
            break

    

    # continue 와 break가 많은 코드는 좋은 코드가 아니다. 

        

    





'''
    num = int(input("1이상 10000이하의 숫자를 입력하세요:"))
    if not 1<num<10000:
        print("잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.")
'''



