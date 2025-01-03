#......namespace....
#.....class namespace
class Mobile:
    fp='yes'
    @classmethod
    def is_fp(cls):
        print('finger print',cls.fp)
realme=Mobile()
redmi=Mobile()
iphone=Mobile()

print('..before modification...')
print('class Fp',Mobile.fp)
print('realme',realme.fp)
print('redmi',redmi.fp)
print('iphone;',iphone.fp)

print('.....after modification of class namespace....')
Mobile.fp='no'
print('class Fp',Mobile.fp)
print('realme',realme.fp)
print('redmi',redmi.fp)
print('iphone;',iphone.fp)

#.....instane namespace....
print('..after modification of instance namespace..')
realme.fp='not working'
print('class Fp',Mobile.fp)
print('realme',realme.fp)
print('redmi',redmi.fp)
print('iphone;',iphone.fp)
