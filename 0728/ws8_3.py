


class PublicTransport:
    
    

    def __init__(self, transport, fare):
        self.transport = transport
        self.fare = fare
        self.passenger_num = 0
        

    def get_in(self, n):
        self.passenger_num += n

    
    def get_off(self, n):
        self.passenger_num -= n

    def profit(self):
        return self.passenger_num * self.fare


p1 = PublicTransport('Taxi' , 4000)
p2 = PublicTransport('Bus' , 1200)

p1.get_in(4)
print(p1.profit())
p1.get_off(2)
print(p1.profit())

p2.get_in(3)
print(p2.profit())


