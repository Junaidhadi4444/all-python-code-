#.....passing and returning set to function...
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s
st={1,2,3,4,'junaid'}
new_st=show(st)
print(new_st)
print(type(new_st))