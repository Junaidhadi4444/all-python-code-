#....access nsted tuple using while loop...
a=(10,20,30,(50,60))
n=len(a)
i=0
while i<n:

    if type(a[i]) is tuple:

        if len(a[i])>1:
            j=0
            m=len(a[i])
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(i,a[i])
        i+=1