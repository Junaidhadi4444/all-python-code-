#.....deleting in ser element...
a={1,2,3,4,'junaid'}
print('original set',a)
print(id(a))

a.remove('junaid')
print('after remving set:',a)
print(id(a))

a.discard('hadi')
print('after remving set:',a)
print(id(a))