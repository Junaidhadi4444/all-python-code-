#.....slicing on array example#2.....
from array import*
stu_roll=array('i',[101,102,103,104,105,106,107,108])
print('origional array')
n=len(stu_roll)
for i in range(n):
    print('i','=',stu_roll[i])
print('********************')
a=stu_roll[0:8:2]
for i in a:
    print(i)
print('********************')
a=stu_roll[0:8:3]
for i in a:
    print(i)