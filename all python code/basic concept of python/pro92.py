#***** passing array to function****
from array import*

def show(arr):
    print(arr)
    print(type(arr))
    for i in arr:
        print(i)
a=array('i',[101,102,103,104])
show(a)