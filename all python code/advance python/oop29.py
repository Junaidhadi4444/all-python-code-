#..... duck typing......
class Duck:
    def walk(self):
        print('thapak thapak thapak')

class Horse:
    def walk(self):
        print('tabbak tabbak tabbak tabbak')

def myfunction(obj):
    obj.walk()
d=Duck()
h=Horse()
myfunction(d)
myfunction(h)