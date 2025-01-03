#.....hierarchical inheritance....
class Father:
    def showf(self):
        print('father class method')

class Son(Father):
    def showS(slf):
        print('son class method')


class doughter( Father):
    def showD(self):
        print('doughtr class method')
s=Son()
s.showf()
s.showS()
d=doughter()
d.showf()
d.showD()