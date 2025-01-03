#.......values method in dict...
stu={101:'yasin',102:'fawad',103:'haseen'}
print('original dict:')
print(stu)
print(type(stu))
print('   ')

all_keys=stu.values()
print(all_keys)
print(type(all_keys))

print(all_keys[0])
print(all_keys[1])
print(all_keys[2])
#...all you can use for loop
for n in all_keys:
    print(n)
