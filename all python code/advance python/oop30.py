#..... 2) strong typing......
class Duck:
    def walk(self):
        print('thapak thapak thapak')

class Horse:
    def walk(self):
        print('tabbak tabbak tabbak tabbak')
        
class Cat:
    def talk(self):
        print('meow meow meow')

def myfunction(obj):
    if hasattr(obj, 'walk'): 
       obj.walk()
    if hasattr(obj, 'talk'):
        obj.talk()
d=Duck()
h=Horse()
c=Cat()
myfunction(d)
myfunction(h)
myfunction(c)