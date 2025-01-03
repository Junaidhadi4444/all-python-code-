#....... tuple of list..
a=(10,20,[30,40])
print('original list A:',a)
print(id(a))
print(type(a))

#...accessing list of tuple using for loop..
n=len(a)
for i in range(n):
    if type(a[i]) is list:

        if(type(a[i]))>1:
            m=len(a[i])
            for j in range(m):

                print(i,j,a[i][j])
    else:
        print(i,a[i])