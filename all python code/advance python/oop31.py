#...method overloading...
class Myclass:
    def Sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s='provide at least two number'
        return s

obj=Myclass()
print(obj.Sum(10, 40))