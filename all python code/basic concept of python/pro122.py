#....accessing nested list using while loop...
a=[10,20,30,[50,60]]

n=len(a)
i=0
while i<n:
    if type(a[i]) is list:
        if len(a[i])>1:
            j=0
            m=len(a[i])
            while i<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1