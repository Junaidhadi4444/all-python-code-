#.....getting input from user- tuple
a=[]
n=int(input('enter number of element:'))
for i in range(n):
    a.append(int(input('enter the element:')))
print(type(a))
a=tuple(a)
print('tuples')
for element in a:
    print(element)
