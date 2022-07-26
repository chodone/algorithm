def de_identify(id_number):
    
    result = ''
    
    print(id(result))

    
    
    result  += id_number[:6]  # result = result + id_number[:6]  -> result의값과 id_number[6:0](얕은복사)의 값을 더한값을 result라는 새로운 id에 저장한다
    print(id(result))
    result  +=  "*******"

    return result , 

print(de_identify('960819-1075811'))

    