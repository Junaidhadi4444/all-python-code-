#...class method without parameter
class Mobile:
    @classmethod            #decorator 
    def show_model(cls):    #class method
        print('realMe x')
    
realme=Mobile()
Mobile.show_model()        #calling class method