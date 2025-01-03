#.....slicing on list.....
x=[101,102,103,104,105,106,107]
print('original list')
n= len(x)
for i in range(n):
    print(i,'=',x[i])

print('from 1st position to 4th position')
a=x[1:5]
for i in a:
    print(i)


print('from 0st position to last position')
b=x[0:]
for i in b:
    print(i)

print('from 0st position to 4th position')
c=x[:5]
for i in c:
    print(i)

print(' last 4 element')
d=x[-4:]
for i in d:
    print(i)

print('from 0th position to 6th position stride 2')
e=x[0:7:2]
for i in e:
    print(i)

print('last 5 element with [-5-(-3)]=2 element towards right')
f=x[-5:-3]
for i in f:
    print(i)