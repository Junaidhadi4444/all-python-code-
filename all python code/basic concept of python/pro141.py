#.....nested tuple...
a=(10,20,30,(50,60))
print(a)
print('using index')
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
#....or...
x=((1,2,3),(4,5,6))
print(x)
print(x[0])
print(x[1])
print("***with index*****")
print(x[0][0])
print(x[0][1])
print(x[0][2])
print(x[1][0])
print(x[1][1])
print(x[1][2])