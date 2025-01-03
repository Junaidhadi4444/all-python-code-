#.....loop controal statement.....
#......while loop....
a=2
while a<=10:
      print(a)
      a+=2
print('rest of the code')
#.......while loop with else......
b=1
while b<=5:
    print(b)
    b+=1
else:
    print('else part executed')
print('rest of the code')
#........nested while loop
i=1
while i<=3:
    print('this is outer loop',i)
    i+=1
    j=1
    while j<=5:
        print("this inner  loop:",j)
        j+=1

