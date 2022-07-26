def test(n,lst):
    n = 10
    lst[1] = 10000
    print(n,lst)

n = 5
lst = [1,2,3]
test(n,lst)
print(n,lst)     

# n은 값을 복사하여 동작
# lst는 id가 넘어가기때문에 같은 데이터 변경이 동시에

n = 5
lst = [1,2,3]
t = lst[::]  #얕은 복사를 통해 넘겨주기
test(n,t)
print(n,lst) 