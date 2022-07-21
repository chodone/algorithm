


word_list = input().split(" ")

check_list = [word_list[0]]

for word in word_list[1:]:
    if check_list[-1][-1] != word[0]:
        print("Fail")
        break
    check_list.append(word)
    
else:
    print("Pass")



