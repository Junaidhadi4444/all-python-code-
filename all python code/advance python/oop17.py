#....static method without parameter 
class Mobile:
    @staticmethod            #decorator 
    def show_model():        #static method 
        print('realMe x')

realme=Mobile()
Mobile.show_model()          # calling static method