#.....slicing on array.....
from array import*
stu_roll=array('i',[101,102,103,104,105,106,107,108])
print('origional array')
n=len(stu_roll)
for i in range(n):
    print('i','=',stu_roll[i])
print('********************')
a=stu_roll[1:5]
for i in a:
    print(i)
print('********************')
a=stu_roll[1:]
for i in a:
    print(i)
print('********************')
a=stu_roll[:5]
for i in a:
    print(i)