#....real use of static method without parameter 
class Mobile:
    @staticmethod            #decorator 
    def show_model(m, p):        #static method 
        model=m
        price=p
        print('model',model,'price',price)

realme=Mobile()
Mobile.show_model('realMe x',1000) # calling static method