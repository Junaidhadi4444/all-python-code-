#.....copying tuple...
a=(10,20,30,-50,21.3,'junaidhadi')
b=a
print(a)
print(b)
print('id of a',id(a))
print('id of b',id(b))
print('   ')
b=a[1:4]
print(a)
print(b)
print('id of a',id(a))
print('id of b',id(b))