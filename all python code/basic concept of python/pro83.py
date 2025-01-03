#****returing lambda fuction from a function***
def add():
    y=2
    return (lambda x:x+y)
a=add()
print(a(1))