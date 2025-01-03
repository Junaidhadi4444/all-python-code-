#....constructor in inheritance...
class Father:
    def __init__(self):
        self.money=1000
        print('father class constructor')
    def show(sel):
        print('father class instance method')

class Son(Father):
    def disp(self):
        print('son class instance method')
s=Son()
print(s.money)
s.show()
s.disp()