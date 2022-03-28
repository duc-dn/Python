# Inheritance trong Python
---
- Tính kế thừa cho phép chúng ta định nghĩa một lớp kế thừa tất cả các phương thức và thuộc tính từ một lớp khác.
```
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Create a class inheritance from class Person 
class Student(Person):
    pass
```