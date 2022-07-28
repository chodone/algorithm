class PublicTransport:
    
    

    def __init__(self, fare):
        
        self.fare = fare
        self.passenger_num = 0
        

    def get_in(self, n):
        self.passenger_num += n

    
    def get_off(self, n):
        self.passenger_num -= n

    def profit(self):
        return self.passenger_num * self.fare


    
class Bus(PublicTransport):
    
    def __init__(self,restrict_num,fare):
        super().__init__(fare)
        self.restrict_num = restrict_num
        self.passenger_num = 0

    def get_in(self, n):
        if self.passenger_num + n > self.restrict_num:
            print('승객을 더이상 태울 수 없습니다')
            
        else:
            self.passenger_num += n
            print(self.passenger_num)

b = Bus(20 , 1200)
b.get_in(12)
b.get_in(10)
print(b.profit())

    