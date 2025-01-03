#....copy list.....
a=[10,20,30,40,50]
b=a.copy()

print(a)
print(b)
print('modifying A:')
a[1]=55
print(a)
print(b)
print('modifying B')
b[3]=66
print(a)
print(b)