#.....2nd method of accessing element of nested list using for loop
a=[[10,20,30],[40,50,60]]
#.....with index..
for r in a:
    for c in r:
        print(c)
    print("  ")
#.....wirth index....
n=len(a)
for i in range(n):

    for j in range(len(a[i])):
        print(i,j, a[i][j])
    print('   ')