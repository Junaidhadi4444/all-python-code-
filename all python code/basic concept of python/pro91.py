#**********function decorator******
def decor(fun):
    def inner():
        print('inner function:before enhancing function')
        fun()
        print('inner function:after enhancing')
    return inner
def num():
    print('we will use this function')
    print('and will inhance this is decorator')
result_fun=decor(num)
result_fun()
#**********easey method  ******
def decor(num):
    def inner():
        print('inner function:before enhancing function')
        num()
        print('inner function:after enhancing')
    return inner
@decor
def num():
    print('we will use this function')
    print('and will inhance this is decorator')
num()
#*****othe rfunction see video 125