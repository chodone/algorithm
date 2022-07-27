import math

def fee(time , mileage):
    hour = time / 60

    insurance_fee = math.ceil(hour) * 2 * 525
    lental_fee = ( time / 10 ) * 1200
    mileage_fee = 0
    if mileage > 100:
        mileage_fee = 170*100 + (mileage - 100)*85
    else:
        mileage_fee = 170 * mileage
    
    total_fee = insurance_fee + lental_fee + mileage_fee

    return int(total_fee)


print(fee(600 , 50))
print(fee(600 , 110))


