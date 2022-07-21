words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
d = {}


for w in words:
    t = ''.join(sorted(w))
    if t in d:
        d[t].append(w)
    else:
        d[t] = [t]
print(d)