string = input()



if len(string) % 2:
    print(string[len(string)//2])
else:
    print(string[len(string)//2 -1] ,string[len(string)//2 ])