#....type of actual argument....
print("*******key word variable length argument****")
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=5,b=11,c=12)