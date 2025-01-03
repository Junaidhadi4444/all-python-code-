#.......formating of string...there are three type of formating string
#...1)c-style string formatting
#.....2)formating string.....
print('********integer*********')
print("{}".format(10))#donot write space between the {}
print('{} {}'.format(10,20))
print('{0}'.format(10))
print('{0} {1}'.format(10,20))
print('{1} {0}'.format(10,20))
print('{num1}'.format(num1=10))
print('{num1} {num2}'.format(num1=10,num2=20))
print('{num2} {num1}'.format(num1=10,num2=20))
#........float.......
print("*********float*********")
print("{}".format(10))#donot write space between the {}
print('{} {}'.format(10.5,20.7))
print('{0}'.format(10))
print('{0} {1}'.format(10.5,20.7))
print('{1} {0}'.format(10.5,20.7))
print('{num1}'.format(num1=10.5))
print('{num1} {num2}'.format(num1=10.5,num2=20.7))
print('{num2} {num1}'.format(num1=10.5,num2=20.7))
#......string....
print('********string***********')
print("{}".format('junaid'))#donot write space between the {}
print('{} {}'.format('junaid','hadi'))
print('{0}'.format('junaid'))
print('{0} {1}'.format('junaid','hadi'))
print('{1} {0}'.format('junaid','hadi'))
print('{str1}'.format(str1='junaid'))
print('{str1} {str2}'.format(str1='junaid',str2='hadi'))
print('{str2} {str1}'.format(str1="junaid",str2='hadi'))
#......integer and string.....
print('************integer and string********')
print('hello my name is: {}'.format('junaid hadi'))
print('{} {}'.format(10,'hadi'))
print('{0} {1}'.format(10,'hadi'))
print('{1} {0}'.format(10,'hadi'))
print('{num1} {str2}'.format(num1=10,str2='hadi'))
print('{str2} {num1}'.format(num1=10,str2='hadi'))
