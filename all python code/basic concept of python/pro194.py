#.....dict comprehesion.....
dict1={}
for n in range(10):
    dict1[n]=n*2
print(dict1)
print('    ')

dict2={n:n*2 for n in range(10)}
print(dict2)
print(' ')

dict2={n:n*2 for n in range(10) if n%2==0}
print(dict2)
print(' ')

dict2={n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict2)
print(' ')
dict2={n:(n if n%2==0 else 'ivalid') for n in range (10)}
print(dict2)