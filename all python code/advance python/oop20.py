#...nested class..
class Army:                   #outer class
    def __init__(self):
        self.name='junaid'
        self.gn=self.Gun()     #creating inner class object
    def show(self):
        print('name',self.name)
    class Gun:
        def __init__(self):
            self.name='ak47'
            self.capacity='75 rounds'
            self.length='34.3 in'
        def disp(self):
            print('gun name:',self.name)
            print('gun name:',self.capacity)
            print('gun name:',self.length)
a=Army()
print(a.name)
a.show()

print(a.gn.name)
#      OR
g=a.gn
print(g.name)
print(g.capacity)
print(g.length)
#     OR
g.disp()