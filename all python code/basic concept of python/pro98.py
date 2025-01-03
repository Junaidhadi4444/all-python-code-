#***** accessing list usinfg for loop
a=[10,20,-50,21.3,'junaidhadi']
print('*****accessing element without index using for loop****')
for element in a:
    print(element)
print("*****accessing element with index using for loop****")
n=len(a)
for i in range(n):
    print(i,a[i])
