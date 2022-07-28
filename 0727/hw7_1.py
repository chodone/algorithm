class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__ (self, name , species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs +=1
        Doggy.birth_of_dogs +=1

    
    def bark(self):
        return f'{self.name}이 월월월월'

    def __del__(self):
        print(f'{self.name}가 운명하셨습니다')
        Doggy.num_of_dogs -= 1
    
    @classmethod
    def get_status(cls):
        return cls.num_of_dogs , cls.birth_of_dogs


dog1 = Doggy("khan" , 'GL')
dog2 = Doggy("wook" , 'Huski')
dog3 = Doggy('hang' , '말티즈')

print(f'num_of_dog : {Doggy.get_status()[0]} \nbirth_of_dog : {Doggy.get_status()[1]} ')
del dog2

print(dog1.bark())
print(f'num_of_dog : {Doggy.get_status()[0]} \nbirth_of_dog : {Doggy.get_status()[1]} ')


# 프로그램을 종료하면서 자연스럽게 인스턴스 메모리를 삭제한다. 그러면서 자동으로 del문 출력