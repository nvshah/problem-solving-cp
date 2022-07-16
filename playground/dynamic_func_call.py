import operator as op

class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age 
    
    def m1(self, num):
        print(num) 

    def m2(self, name, age):
        print(name, ' ', age)

p = Person("manan", 20) 



# attrs = ['Person', 'm1', 'm2']
# params = [[], [30], ['Ashsisj', 39]]

# obj = 

# for a, p in zip(attrs, params):
#     op.methodcaller
