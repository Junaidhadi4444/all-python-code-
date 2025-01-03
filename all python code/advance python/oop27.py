#.....multiple inheritance...
class Father:
    def showF(self):
        print('father class method')

class Mother:
    def showM(self):
        print('mother class method')
class Son(Father, Mother):
    def showS(self):
        print('child class method')


s=Son()
s.showF()
s.showM()
s.showS()