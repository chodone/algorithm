words = ["round" , "dream" , "magnet" , "tweet" , "tweet" , "trick" , "kiwi" ,"done"]

pass_words = [words[0]]
cnt = 1

for word  in words[1:]:
    if word in pass_words:
        print(f"이전에 등장했던 단어입니다. {cnt}번째 사람 탈락!")
        break
    elif pass_words[-1][-1] != word[0]:
        
        print(f"앞서 입력된 마지막 문자와 일치하지 않습니다.  {cnt}번째 사람 탈락!")
        break
    elif word == "done":
        print("done이 입력되었으므로 종료합니다")
        break
    pass_words.append(word)
    cnt += 1


