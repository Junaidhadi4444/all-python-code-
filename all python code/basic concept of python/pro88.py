#*****global function******
a=10
def show():
    b=50
    print('globale function:',a)
    x=globals()['a']
    print('x:',x)
show()