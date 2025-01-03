#......formatting string.....
#.....integer....from format spacification
print('*******integer*******')
print('{num:d}'.format(num=15))
print('{num:5d}'.format(num=15))#5d means create 5 boxes
print('{num:05d}'.format(num=15))#0 means fill three zero from the empty space
print('{num:+5d}'.format(num=15))
print('{num:<5d}'.format(num=15))#   < mean move left align
print('{num:*<5d}'.format(num=15))
print('{num:*>5d}'.format(num=15))
print('{num:^5d}'.format(num=15))#  ^ mean move to center 
print('{num:*^5d}'.format(num=15))
#.......float.....
print("************float*************")
print('{}'.format(15.33))
print('{:f}'.format(15.33))
print('{0:f}'.format(15.33))
print('{num:f}'.format(num=15.33))
print('******format spacification for float******')
print('{num:f}'.format(num=15.33))
print('{num:8f}'.format(num=15.33))
print('{num:8.3f}'.format(num=15.33))
print('{num:+8.3f}'.format(num=15.33))
print('{num:<8.3f}'.format(num=15.33))
print('{num:*<8.3f}'.format(num=15.33))
print('{num:*>8.3f}'.format(num=15.33))
print('{num:^8.3f}'.format(num=15.33))
print('{num:*^8.3f}'.format(num=15.33))
#***********format spacificatiopn for float*****
print('******string******')
print('{:10s}'.format('junaid'))
print('{:<10s}'.format('junaid'))
print('{:*<10s}'.format('junaid'))
print('{:>10s}'.format('junaid'))
print('{:*>10s}'.format('junaid'))
print('{:^10s}'.format('junaid'))
print('{:*^10s}'.format('junaid'))
print('*******slicing********')
print('{:10.3s}'.format('junaidhadi'))# left right and center use upper method