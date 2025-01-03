
#.....Nested dict in python....
#....creating nested dict with element...
a={'course':'python','fees':14000,1:{'course':'javascript','fees':20000}}

print(a['course'])
print(a['fees'])

print('the nested dict is:')
print(a[1])

print(a[1]['course'])
print(a[1]['fees'])