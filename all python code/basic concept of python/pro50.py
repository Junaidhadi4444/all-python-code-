#..... accessing loop.....
#......using for loop with out index...
str1='junaid'
for c in str1:
    print(c)
#.....using for loop but access through index....
str2='junaid'
n=len(str2)
for i in range(n):
    print(str2[i])
#.....using while loop
str3='junaid'
n=len(str3)
i=0
while i<n:
    print(str3[i])
    i+=1