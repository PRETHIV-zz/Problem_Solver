# Hello World program in Python
#guvi this is rocky
#rockys aim is getting output without using a single variable
a=input()
l=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in a:
    for j in l:
        if i==j:
            c+=1
if c==0:
    print("no")
else:
    print("yes")
