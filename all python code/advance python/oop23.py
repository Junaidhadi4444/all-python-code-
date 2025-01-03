#....constructor overriding....
class Father:
    def __init__(self):
        self.money=2000
        print('father class constructor')

    def show(self):
        print('father class instanace method')

class Son(Father):
    def __init__(self):
        self.money=3000
        self.car='BMW'
        print('son class constructor')
    def disp(self):
        print('son class instnce method')
f=Father()
s=Son()
print(s.money)
print(s.car)
s.disp()
s.show()