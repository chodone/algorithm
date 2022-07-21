'''

from curses.ascii import isupper
import re

s = input().split(" ")


for i in s:

    new_string = re.sub(r"[^a-zA-Z0-9,.]","",i)   #정규표현식 공부
    print(new_string.lower() ,end=" ")

'''

strV = '@#~I Never DREeamed Tas, Tffff !>!'
result = ''


for ch in strV:
    if ch.isalpha() or ch == ' ' or ch ==",":
        result += ch
print(result)
result1 = ''
isFirstT = True
for ch in result:
    if ch.isupper():
        if ch == 'T' and isFirstT:
            result1 += 'T'
            isFirstT = False
        else:
            result1 += ch.lower()
    else:
        result1 += ch


print(result1)




