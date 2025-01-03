#....access nsted tuple using for loop...
a=(10,20,30,(50,60))
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:

        if(type(a[i]))>1:
            m=len(a[i])
            for j in range(m):

                print(i,j,a[i][j])
    else:
        print(i,a[i])
#......OR......

b=(1,2,3),(4,5,6)
#.....with out indx...
for r in b:
    for c in r:
        print(c)
    print('  ')
