crop_list = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

sortcrop_list = sorted(crop_list, key= lambda x:x[1])

print(sortcrop_list[-1][0])