infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
sum = 0


for dict_a in infos:
    for key in dict_a.keys():
        if key == 'age':
            sum += dict_a[key]

print(sum)
