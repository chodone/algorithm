

class Stack:

    stack_lst = []

    def __init__(self):
        pass
        

    @classmethod
    def empty(cls):
        if len(cls.stack_lst) == 0:
            return True
        else:
            return False
    
    @classmethod
    def top(cls):
        return cls.stack_lst[-1]
    
    @classmethod
    def pop(cls):
        if len(cls.stack_lst) == 0:
            return None
        else:
            result = cls.stack_lst.pop()
            cls.stack_lst.clear()
            return result
    @classmethod
    def push(cls, a):
        cls.stack_lst.append(a)

    @classmethod
    def __repr__(cls) :
        return str(cls.stack_lst)


s1 = Stack()
s2 = Stack()
s3 = Stack()

s1.push(1)
s1.push(2)

s1.push(2)
s1.push(3)

s1.push(3)
s1.push(2)

print(repr(s1))
print(repr(s2))
print(repr(s3))







