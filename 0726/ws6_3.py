def count_vowels(s):
    

    cnt = 0
    # 모음을 판별하는 함수? -> X
    vowels_lst = ['a','e','i','o','u']
    for alp in s:
        if vowels_lst.count(alp):
            cnt += 1
        
    return cnt
        






print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3