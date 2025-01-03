
#..... multi-level inheritance....
class Father:
    def showF(self):
        print("parent class method")


class Son(Father):
    def showS(Father):
        print('son class method')

class Grandson(Son):
    def showG(self):
        print('gandson class method')

g=Grandson()
g.showF()
g.showG()
g.showS()