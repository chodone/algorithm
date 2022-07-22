blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_names = list(set(blood_types))

blood_dict = {}


for key in blood_names:
    cnt = 0
    for bloodtype in blood_types:
        if key == bloodtype:
            cnt += 1
    blood_dict[key] = cnt

print(blood_dict)
