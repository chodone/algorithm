# 괄호검사



for tc in range(int(input())):
    test_lst = input() 
    stack_lst = []  # 여는 괄호가 나오면 담을 stack_lst

    for ele in test_lst:
        #여는 괄호
        if ele == '(' or ele == '{':
            stack_lst.append(ele)

        #닫는 괄호
        elif ele == ')':
            if not stack_lst or stack_lst[-1] != '(':  # 빈스택 or 닫는괄호가 여는괄호(stack top이)랑 매칭되지 않을때 바로 탈출
                print(f'#{tc+1} 0')
                break
            else:
                stack_lst.pop() # 닫는괄호 여는괄호 일치시 스택 top 삭제 
        elif ele == '}':
            if not stack_lst or stack_lst[-1] != '{':  # 빈스택 or 닫는괄호가 여는괄호(stack top이)랑 매칭되지 않을때 바로 탈출
                print(f'#{tc+1} 0')
                break
            else:
                stack_lst.pop() # 닫는괄호 여는괄호 일치시 스택 top 삭제 
                

        # 다른 문자         
        else:
            continue
    else:
        if not stack_lst:
            print(f'#{tc+1} 1')

        else:
            print(f'#{tc+1} 0')



# 첫번째 바보짓 - 괄호가 뒤집어진다는것 왜 생각 못했을까.. print문으로 해결;;
# 두번째 바보짓 - 런타임 에러.. 닫는괄호에서  빈스택이 발생할때 탈출하지 못하는 코드를 짜서 발생.. 