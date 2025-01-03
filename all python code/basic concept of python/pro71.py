#.....return statement....
#......return single value.....
print('*******return single value********')
def add():
    x=10
    y=20
    z=x+y
    return z
sum=add ()
print(sum)
print("********return multiple value****")
def add(b):
    a=12
    c=a+b
    d=a-b
    return c,d
sum,sub=add(13)
print(sum)
print(sub)

