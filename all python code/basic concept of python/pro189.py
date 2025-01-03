#....passing and reruring dict...
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k,'=',d[k])
    return d
dc={101:'junaid',102:'fawad',103:'izhar'}
new_dc=show(dc)
print(type(new_dc))