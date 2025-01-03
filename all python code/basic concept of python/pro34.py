#.....pop() function and pop(positionNumber).......
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print('array after pop')
stu_roll.pop(1)
i=0
while i<n:
    print(stu_roll[i])
    i+=1

