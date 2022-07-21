score = {'python' : 80 , 'django' :89 , 'web' : 83}
score['algorithm'] = 90
score['python']  = 85
print(score)

sum = 0
avg = 0

for i in score:
    sum += score[i]

avg = sum / len(score)
print(avg)
