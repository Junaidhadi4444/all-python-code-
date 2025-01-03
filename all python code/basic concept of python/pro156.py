#.....getting input from user...
a=set()
print(id(a))
n=int(input('enter number of element:'))
for i in range(n):
    e1=input('enter element:')
    a.add(e1)
print(a)
print(id(a))