#......method resolution order...
class Father:
    def __init__(self):
        super().__init__()
        print('father class constructor')
    def showF(self):
        print('father class method')


class Mother:
    def __init__(self):
        super().__init__()
        print('mothr class constructor')
    def showM(self):
        print('mother class method')


class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print('son class constructor')
    def show(self):
        print('son class method')

s=Son()