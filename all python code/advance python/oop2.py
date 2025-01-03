#....constructor.....
#.....example number 3....
print('   ')
class mobile:
    def __init__(self):   # constructor with out parameter
        self.model='realme X'
    def show_model(self):
        price=10000
        print('model:',self.model, 'price',price)
realme=mobile()
realme.show_model()
print('   ')

#.....example number 4....
class mobile:
    def __init__(self):
        self.model='realme X'
    def show_model(self):
        print('model:',self.model)
realme=mobile()
print(realme.model)