words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

antonym_words = []

# 내가 얻고자 하는 값들은 키에 있으므로 키값들을 뽑아낸다
for word in words_dict.keys():
    if word[0] == 'b' or word[0] == 'm' or word[0] == 'p':
        antonym_words.append('im' + word)
    elif word[0] == 'l':
        antonym_words.append('il' + word)
    elif word[0] == 'r':
        antonym_words.append('ir' + word)
print(sorted(antonym_words)) 
