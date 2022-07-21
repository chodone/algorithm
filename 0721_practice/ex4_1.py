

password = '8797' 

for i in range(3):
    user_password = input()
    if user_password == password:
        print("로그인 성공")
        break

else:
    print("비밀번호를 3회이상 잘못 입력하여 종료합니다.")

