print('*************logical AND operator*************')
a=5
b=2
c=3
d=200
w=(a>b)and(a>c)
x=(a>b)and(a<c)
y=(a<b)and(a>c)
z=(a<b)and(a<c)
print(w)
print(x)
print(y)
print(z)
#true
print((a>b) and c)
print((a>b)  and  c and d)
#false
print((a<b) and c)
print((a<b) and c and d)
print('**************logical OR operator************')
w=(a>b)or(a>c)
x=(a>b)or(a<c)
y=(a<b)or(a>c)
z=(a<b)or(a<c)
print(w)
print(x)
print(y)
print(z)
#true
print((a>b) or c)
print((a>b)  or  c or  d)
#false
print((a<b) or  c)
print((a<b) or  c or d)
print("**************** NOT operator********")
x=a<b
y=a>b
print(not(x))
print(not(y))