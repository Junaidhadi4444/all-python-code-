#....copying set element...
a={1,2,3,4,'junaid'}
print(a)
print(id(a))
new_a=a.copy()
print('after copy:',new_a)
print(id(new_a))