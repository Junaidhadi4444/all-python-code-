#......getting input from the user using for loop...
from array import*
stu_roll=array('i',[])
n=int(input('enter number of element:'))
for i in range(n):
    stu_roll.append(int(input('enter elememt:')))
for i in range(len(stu_roll)):
    print(stu_roll[i])