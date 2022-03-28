# Class in Python
--- 
- `__init__()` là 1 hàm đã được Python built-in  
- Tất cả các lớp đều có một hàm được gọi là `__init__()`, hàm này luôn được thực thi khi lớp đang được khởi tạo.
- Sử dụng hàm `__init__()` để gán giá trị cho các thuộc tính đối tượng hoặc các thao tác khác cần thực hiện khi đối tượng đang được tạo
- Note: Hàm `__init__()` được gọi tự động mỗi khi lớp được sử dụng để tạo một đối tượng mới
> Note: 
> - Tham số self là một tham chiếu đến lớp hiện hiện tại và được sử dụng để truy cập các biến thuộc về lớp.
> - Có thể gọi nó bất cứ thứ gì bạn thích, nhưng nó phải là tham số đầu tiên của bất kỳ hàm nào trong lớp

```
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

person = Person("Duc", 22);
print("Name: {}, Age: {}".format(person.name, person.age))
```
### Methods in a class/object
---
- Các đối tượng cũng có thể chứa các phương thức. Các phương thức trong đối tượng là các hàm thuộc về đối tượng.
```
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is {}".format(self.name))
```
## Modify Object Properties
---  
```
person.age = 24;
```
## Delete Object Properties
```
del person.age
```
## Delete Objects
```
del person
```