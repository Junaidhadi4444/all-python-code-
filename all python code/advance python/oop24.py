#.....constructor with super method.....
class Father:
    def __init__(self,m):
        self.money=m
        print('father class constructor')
    def show(self):
        print('father class instance method')

class Son(Father):
    def __init__(Self,m):
        super().__init__(m) #calling parent class constructor
        print('son class constructor')
    def show(self):
        print('son class instance method',self.money)
s=Son(2000)
s.disp()