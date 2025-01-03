#......items method method in dict....
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dict:')
print(stu)
print('   ')
it=stu.items()
print(it)
print(type(it))
print('   ')
lst=list(it)
print(lst)
print(type(lst))
print('   ')

print(lst[0])
print(lst[0][0])
#.....using nested for loop..
for r in lst:
    for c in r:
        print(c)