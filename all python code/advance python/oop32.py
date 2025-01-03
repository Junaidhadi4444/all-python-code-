#.....method overriding.....
class Add:
    def result(self, x, y):
        print('addition',x+y)
        
class Multi(Add):
    def result(self, a, b):
        super().result(10, 20)
        print('mutiplication',a*b)
    
m=Multi()
m.result(10, 20)