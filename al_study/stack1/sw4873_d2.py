# 반복문자 지우기

for tc in range(int(input())):
    check_str = input()
    stack_lst = [] 

    for alp in check_str:  
        if not stack_lst or alp != stack_lst[-1]:   #빈스택일때 IndexError가 발생한다!!!!! - 제발 정신좀 차려라
            stack_lst.append(alp) # top과 같지 않을 시 stack에 추가
        else:
            stack_lst.pop() # top과 같을 시 pop()으로 top 삭제

    


    print(f'#{tc+1} {len(stack_lst)}')


    # 첫번째 바보짓 - list(str) 시 자동으로 문자하나씩 순회하면서 list형태로 만들어준다;;
    # 두번째 바보짓 - 빈 스택일때 자꾸 생각 안해서 IndexError 발생
    


    



    



# 첫번째 바보짓 - 처음 3문자가 연속으로 나올 시 error가 발생하게 코딩;
'''

for tc in range(int(input())):
    check_str = input()
    stack_lst = [check_str[0]] # 처음 알파벳을 넣은 이유 - 빈 리스트로 시작할시 IndexError가 발생한다

    for alp in check_str[1:]:  # 처음 알파벳을 넣기 때문에 인덱스1부터 순회시작
        if alp != stack_lst[-1]:
            stack_lst.append(alp) # top과 같지 않을 시 stack에 추가
        else:
            stack_lst.pop() # top과 같을 시 pop()으로 top 삭제

    print(f'#{tc+1} {len(stack_lst)}')
'''