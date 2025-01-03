#....list comprehension......
lst1=[i for i in range(20)]
print(lst1)
print('      ')

lst2=[i+1 for i in range(20)]
print(lst2)
print('  ')

print('*******print even number*****')
lst3=[i for i in range(20) if i%2==0]
print(lst3)
print('  ')

print('*******print number*****')
lst4=[i for i in range(20) if i%2==0 if i%3==0]
print(lst4)
print('  ')

print('*******print number*****')
lst5=[i if i%2==0 else 'invalid' for i in range(10)]
print(lst5)
print('  ')