#.......popitem method in dict...
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dict:')
print(stu)
print(id(stu))
print('   ')
removed_item=stu.popitem()
print('after removing dict')
print(stu)
print(id(stu))
print('   ')
print('the remived value is:',removed_item)