#......deleting...
stu={101:'yasin',102:'fawad',103:'haseen'}
print('before deletion')
print(stu)
print(id(stu))

del stu[102]
print('after  deletion')
print(stu)
print(id(stu))
del stu
#print('after  deletion dic')
#print(stu)   its show error because dic is
