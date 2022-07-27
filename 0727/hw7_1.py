class Doggy():
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__ (self, name , species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs +=1
        Doggy.birth_of_dogs +=1

    @staticmethod
    def bark():
        return '월월월월'
    
    @classmethod
    def get_status(cls):
        return cls.num_of_dogs , cls.birth_of_dogs


dog1 = Doggy("khan" , 'GL')
dog2 = Doggy("wook" , 'Huski')

print(f'num_of_dog : {Doggy.get_status()[0]} \nbirth_of_dog : {Doggy.get_status()[1]} ')
print(dog1.bark())