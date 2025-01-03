#....class variable or static varibale
class Mobile:
    fp='yes'      #class variable
    def __init__(self):
        self.model='realme x'   #instance variable
    def show_model(self):       #instance method
        print('model',self.model) # accessing instance variabel
    @classmethod                  # class method
    def is_fp(cls):
        cls.fp
        print('finger print',cls.fp)    #access class variable
realme=Mobile()
realme.show_model()
Mobile.is_fp() 
print(' ')           

# modify out side of the class
Mobile.fp='no'
Mobile.is_fp()   