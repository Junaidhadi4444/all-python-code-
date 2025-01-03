#....operator overloading....
from re import X


class A:
    def __init__(self, other):
        self.x=X
    def __add__(self, other):
        return self.x + other.x


class B:
     def __init__(self, other):
        self.x=X
        
a=A(1)
b=B(2)
print(a+b)    