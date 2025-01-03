#....single inheritnce...
class Father:
    money=1000
    def show(self):
        print('parent class instance method')
    @classmethod
    def showmoney(cls):
        print('parent class class method:',cls.money)
    @staticmethod
    def stat():
        a=20
        print('parent class static method',a)
class Son(Father):
    def disp(self):
        print('child class intstance method')
s=Son()
s.disp()
s.show()
s.showmoney()
s.stat()