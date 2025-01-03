#*******pass or call by obj refrence******
def val(x):
    print(x,id(x))
    x=15
    print(x,id(x))
x=10
val(x)
print(x,id(x))
#******** scond exmaple
def val(lst):
    lst.append(4)
    print(lst,id(lst))
lst=[1,2,3]
print(lst,id(lst))
val(lst)
print(lst,id(lst))
