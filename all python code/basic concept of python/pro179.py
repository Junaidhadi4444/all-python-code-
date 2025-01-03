#.....getting dict input from user.....
a={}
n=int(input('enter number of element:'))

for i in range(n):
    k=input('enter key:')
    v=input('enter value:')
    a.update({k:v})
print(a)
#...create alittle mistake
