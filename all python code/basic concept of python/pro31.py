#........accessing array with for loop....
#.......example no#1....
from array import*
stu_no=array('i',[101,102,103,104,105])
for element in stu_no:
    print(element)
#.......2nd method accessing element with the help of index...
from array import*
stu_no=array('i',[101,102,103,104,105])
n=len(stu_no)
for i in range(n):
    print("index",i,"=",stu_no[i])