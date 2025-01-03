#....passing and returing tuple to function..
def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
        return t
tup=(10,20,30,21.3,'junaidhadi')
new_tup=show(tup)
print(new_tup)
print(type(new_tup))