#.......list of tuple..
a=[10,20,(30,40)]
print('original list A:',a)
print(id(a))
print(type(a))
#****appending a new tuple*****
a.append((50,60))
print('after appending',a)
print(id(a))
print(type(a))
#...accessing list of tuple using for loop..
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:

        if(type(a[i]))>1:
            m=len(a[i])
            for j in range(m):

                print(i,j,a[i][j])
    else:
        print(i,a[i])