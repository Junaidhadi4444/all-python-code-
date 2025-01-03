#...accessinf nested dict ....method 2

a={
    1:{'course':'python','fees':14000},
    2:{'course':'javascript','fees':20000}
}
print(a)
print(a[1])
print(a[2])

print('....after mdifying...')
a[1]['course']='machine learning'
print(a)
print('....deleting element in dict...')
del a[1]['course']
print(a)
#.....see more detailes in method first...
