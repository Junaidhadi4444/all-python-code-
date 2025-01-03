#....accessing nested element using for loop..method2
a={
    1:{'course':'python','fees':14000},
    2:{'course':'javascript','fees':20000}
}
print('ID:')
for id in a:
    print(id)

#....keys...
print('keys')
for id in a:
    for k in a[id]:
        print(k)
#...keys in values...
print('keys and values')
for id in a:
    for k in a[id]:
        print(k,a[id][k])  