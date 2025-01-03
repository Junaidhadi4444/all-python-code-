#......sets method....
a={'yasin','haseen','junaid','izhar'}
b={'junaid','farid','sajid','israr'}
print(a)
print(b)
print('  ')
print('******intersection******')
ism=a.intersection(b)
print(ism)
ism=a.intersection(b)
print('  ')
print('******union******')
u=a.union(b)
print(u)
print('  ')
print('******diffrence******')#  only contain in set a...
d=a.difference(b)
print(d)
print('  ')
print('******issubset******')
c=a.issubset(b)
print(c)
print('  ')
print('******isssuperset******')
e=a.issuperset(b)
print(e)


