#......extend() function.....
from array import*
stu_roll=array('i',[101,102,102,103,104])
arr=array('i',[106,107,108,109])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
print("array after extend")
stu_roll.extend(arr)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1