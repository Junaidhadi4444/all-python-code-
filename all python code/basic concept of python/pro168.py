#....copy nethod in dict....
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dic:')
print(stu)
print(id(stu))

new_stu=stu.copy()
print('copied dic')
print(new_stu)
print(id(new_stu))
