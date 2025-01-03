# ...constructor.....
#.....example number 6 with parameter....
print('   ')
class Mobile:
    def __init__(self,m):   # constructor with parameter
        self.model=m
    def show_model(self,p):
        price=p
        print('model:',self.model, 'price',price)
realme=Mobile('realme X')
realme.show_model(10000)
print(id(realme))
print('   ')

redmi=Mobile('redmi 7s')
redmi.show_model('200000')
print(id(redmi))