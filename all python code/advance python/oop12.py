#....instance method with parameter....
class Mobile:
    def __init__(self):
        self.model='real me x'     #instance variable 
    #instance method
    def show_model(self,p):
        self.price=p
        print('model:',self.model,'price:',self.price)
realme=Mobile()
realme.show_model(100)