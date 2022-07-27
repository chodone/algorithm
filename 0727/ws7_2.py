
def wordrelay(words):
    
    pass_words = [words[0]]
    cnt = 2

    for word  in words[1:]:
        if word in pass_words:
            return f"이전에 등장했던 단어입니다. {cnt}번째 사람 탈락!" 
            
        elif pass_words[-1][-1] != word[0]:
        
            return f"앞서 입력된 마지막 문자와 일치하지 않습니다.  {cnt}번째 사람 탈락!"
            
        elif word == "done":
            return "done이 입력되었으므로 종료합니다"
            
        pass_words.append(word)
        cnt += 1


words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.