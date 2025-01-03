#*******getting list input from the user****
a=[]
print(a)# empty list
n=int(input('enter number of element:'))
for i in range(n):
    a.append(int(input('enter element:')))
print('list:')
for element in a:
    print(element)