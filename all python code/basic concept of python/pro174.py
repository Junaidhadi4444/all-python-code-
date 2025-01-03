#.......update method in dict...
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dict:')
print(stu)
print(id(stu))
print('   ')

vals={'name':'junaid','address':'kamartall'}
#stu.update({104:'junaid'})
stu.update(vals)
print(stu)
print(id(stu))

