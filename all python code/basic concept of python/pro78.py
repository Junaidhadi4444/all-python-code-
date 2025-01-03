#....type of actual argument....
print('********variable length arument*****')
def add(*num):
    z=num[0]+num[1]+num[2]
    print('addition:',z)
add(3,4,5)