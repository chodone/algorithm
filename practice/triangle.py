for i in range(7):
    for k in range(7,i,-1):
        print(' ',end='')

    for k in range((i+1)*2-1):
        print("*",end='')
    print()