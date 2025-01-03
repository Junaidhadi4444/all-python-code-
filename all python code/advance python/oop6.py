#.....example number 6 with parameter....
print('   ')
class Mobile:
    #constructor with parameter
    def __init__(self,m, v=80):
        self.model=m
        self.volumn=v
    def show_model(self,p):
        price=p      #local variable
        print('model:',self.model, 'price',price)
        print('volumn:',self.volumn)
# passing argument to constructor
realme=Mobile('realme X')
# accessing method from outside of the class
realme.show_model(10000)