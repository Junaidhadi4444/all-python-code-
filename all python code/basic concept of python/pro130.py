#.....generator function
#.....yield statement...
#......next function....
from unittest import result


def disp(a,b):
    yield a
    yield b
result=disp(10,20)
print(result)
print(type(result))

print(next(result))
print(next(result))
#.....using loop
def show(x,y):
    while x<=y:
        yield x
        x+=1
n=show(1,5)
print(n)
print(type(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))