# Hello World program in Python
#guvi this is rocky
s=input()
c=0
for i in s:
    if i=="0" or i=="1":
        continue
    else:
        c+=1
if c==0:
    print("yes")
else:
    print("no")
