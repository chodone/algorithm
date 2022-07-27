class Calculator():

    def __init__(self , a,b) :
        self.a = a
        self.b = b

    def add(self):  # 인스턴스 메서드
        return self.a + self.b
    def substrack(self): # 인스턴스 메서드
        return self.a - self.b
    def multiply(self): # 인스턴스 메서드
        return self.a * self.b
    def divide(self): # 인스턴스 메서드
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다'



test1 = Calculator(2,3)
test2 = Calculator(2,1)
test3 = Calculator(3,4)
test4 = Calculator(4,0)

print(test1.add())
print(test2.substrack())
print(test3.multiply())
print(test4.divide())