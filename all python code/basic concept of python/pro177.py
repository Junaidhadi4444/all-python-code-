#.......setdefault method in dict...
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dict:')
print(stu)
print(id(stu))
print('   ')

returned_value=stu.setdefault(104,'python')
print(returned_value)
returned=stu.setdefault(101)
print(returned)

