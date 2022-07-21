num_list = list(range(1,1001))

sum = 0

two = num_list[1::2]


seven = num_list[6::7]


for i in two:
    sum += i

for i in seven:
    sum += i

print(sum)