#....slicing tuple.....
x=((10,20,30,),
   (40,50,60),
   (70,80,90),
   (11,22,33),
   (44,55,66),
   (77,88,99),
   (12,13,14))
print('original tuple')
print(x)
print('from first position to 4th position')
a=x[1:5]
print(a)
print('from 0th position to last position')
b=x[0:]
print(b)
print('from 0th position to 4th position')
c=x[:5]
print(c)
print('last 4 tuple')
d=x[-4:]
print(d)
print('from 0th position to 6th position stride 2')
e=x[0:7:2]
print(e)
print('last 5th element with [-5-(-3)]=2 elements towaed right')
f=x[-5:-3]
print(f)