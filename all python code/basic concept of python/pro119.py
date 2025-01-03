#......modifing nested list......
a=[10,20,30,[40,50]]

print('before modification A')

print(a)

a[1]=1
a[3][0]=2

print('after modification')

print(a)