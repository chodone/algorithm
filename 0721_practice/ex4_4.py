word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

sum1 = 0
sum2 = 0

for i in word1:
    sum1 += ord(i)



for i in word2:
    sum2 += ord(i)

if sum1 > sum2:
    print(word1)
elif sum1 < sum2:
    print(sum2)
else:
    print("두 문자의 아스키코드값의 값이 같습니다")

# ord()는 문자열의 아스키 코드값을 반환하는 함수
# chr()은 아스키 코드를 문자열로 반환하는 함수


