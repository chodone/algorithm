
for tc in range(int(input())):
    N = int(input())

    card_list = [0]*10

    cards = list(map(int, input()))

    for card in cards:
        card_list[card] += 1

    
    max = [0,0]
    idx = 0
    for num in card_list:
        if num > max[1]:
             
            max[0] = idx
            max[1] = num
        elif num == max[1]:
            if max[0] < idx:
                max[0] = idx
        idx += 1

        

    print(f'#{tc+1} {max[0]} {max[1]}')