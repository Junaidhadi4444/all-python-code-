#....instance variable...
class Mobile():
    def __init__(self):          #constructor
        self.model='realme X'    # instance variable
    def show_model(self):
        print(self.model)        #accessing instance variable
realme=Mobile()
redmi=Mobile()
iphone=Mobile()
print(realme.model)
print(redmi.model)
print(iphone.model)
print('  ')

redmi.model='redmi 7s'
print(realme.model)
print(redmi.model)
print(iphone.model)
print('  ')