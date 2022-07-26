words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anaList = [[]]


# for word in words:
#     t = ''.join(sorted(word))
#     if not t in anaList:
#         anaList.append(t)

# print(anaList)



for word in words:
    t = ''.join(sorted(word))
    for d in anaList:
        if t == sorted(d[0]):
            d.append(word)
        else:
            anaList.append([word])

print(anaList)