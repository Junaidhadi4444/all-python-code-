#.....hight order function...
#....filter function
a=[50,60,80,90,5,45,65]

def hight_marks(n):
    if n>=60:
        return True

result=filter(hight_marks,a)
print(result)
print(type(result))