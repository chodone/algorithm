


class Person:
    name = False
    age = False

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    @classmethod
    def detail(cls, name, birth):
        age = 2022 - birth

        return Person(name , age)

    def check_age(self):
        if self.age < 19:
            return True
        else:
            return False


person1 = Person('조성욱' , 27)

print(person1.check_age())
a =  Person.detail('조영연' , 2017 )
print(a.check_age())


        



