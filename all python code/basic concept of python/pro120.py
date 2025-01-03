#.....accessing nested list using for loop...

a=10,20,30,[40,50]
n=len(a)       #count NO of element in A n=4
for i in range(n):
    if type(a[i]) is list:   # cheak a[i] is a list type or not
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])
