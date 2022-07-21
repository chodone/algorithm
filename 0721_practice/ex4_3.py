number_list = list(map(int , input()))

new_number_list = []

for i in number_list:
    if  i in new_number_list:
        continue
    else:
        new_number_list.append(i)

print(new_number_list)
