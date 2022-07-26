strV = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'
result = ''


for ch in strV:
    if ch.isalpha() or ch == ' ' or ch ==",":
        result += ch

result1 = ''
isFirstI = True
for ch in result:
    if ch.isupper():
        if ch == 'I' and isFirstI:
            result1 += 'I'
            isFirstT = False
        else:
            result1 += ch.lower()
    else:
        result1 += ch


print(result1)