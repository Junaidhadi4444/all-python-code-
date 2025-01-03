#.....accessing Nested dict in python
a={'course':'python','fees':14000,1:{'course':'javascript','fees':20000}}
for i in a:
    print(i)
#....accessing each id keys--values
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k,'=',a[i][k])
    else:
        print(i,'=',a[i])