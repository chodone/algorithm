from curses.ascii import isupper
import re

s = input().split(" ")


for i in s:

    new_string = re.sub(r"[^a-zA-Z0-9,.]","",i)   #정규표현식 공부
    print(new_string.lower() ,end=" ")



