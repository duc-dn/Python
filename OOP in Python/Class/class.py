# class MyClass:
#     x = 5

# p1 = MyClass()
# print("x = {}".format(p1.x))

class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is {}".format(self.name))

    

person = Person("Duc", 22);

print("Name: {}, Age: {}".format(person.name, person.age))
person.myFunc();

# Modify Object Properties
person.age = 24;
print(person.age)

# Delete object properties
del person.age
print(person.age)
