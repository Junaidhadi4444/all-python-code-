#*********#***** returning array to function****
from array import*

def show(arr):
    print("passing array arr",arr)
    print(type(arr))
    for i in arr:
        print(i)
    return arr
a=array('i',[101,102,103,104])
y=show(a)
print("returning array Y:",y)
print(type(y))
for i in y:
    print(i)
