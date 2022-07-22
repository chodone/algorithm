
def salt(salty , salt_water):
    totalsalt =  (salty*salt_water) / 100
    return totalsalt

def density(salt , salt_water):
    salt_density = (salt/salt_water) * 100
    return salt_density


salt_list = []
for i in range(5):
    
    saltcase = []
    a = input().split(" ")
    
    if a[0] == 'Done':
        break
    else:
        salty , salt_water = map(int , a)
        saltcase.append(salt(salty , salt_water))
        saltcase.append(salt_water)
        salt_list.append(saltcase)

sumsalt = 0
sumwater = 0


for case in salt_list:
    sumsalt += case[0]
    sumwater += case[1]

print(round(density(sumsalt, sumwater), 2)  , round(sumwater , 2) )




    
