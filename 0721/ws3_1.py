fruit_list = input().split(",")

# apple,rottenBanana,apple,RoTTenorange,Orange

new_fruit_list = []
for fruit in fruit_list:
    
    if  fruit.lower()[:6] == 'rotten':
        new_fruit_list.append(fruit.lower()[6:])
        
    else:
        new_fruit_list.append(fruit.lower())

print(new_fruit_list)


