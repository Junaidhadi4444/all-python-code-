#....accessing tuple using for loop...
a=(10,20,30,-50,21.3,'junaidhadi')
print('acceswsing element using for loop but with out index')
for element in a:
    print(element)
print('***with index....****')
n=len(a)
for i in range(n):
    print(a[i])