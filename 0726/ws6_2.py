grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

sortgrain_lst = sorted(grain_lst, key= lambda x:x[1])     # sorted 함수는 원본에 영향을 주지 않고 새로운 값을 생성한다!! 
                                                          # lambda 사용법 잊지말자                                        
print(sortgrain_lst[-1][0])


