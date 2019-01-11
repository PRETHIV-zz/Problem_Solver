# Hello World program in Python
#guvi this is rocky
s=input()
c=0
for i in s:
    if i.isalpha():
        c+=1
        break
for i in s:
    if i.isnumeric():
        c+=1
        break
if c==2:
    print("Yes")
else:
    print("No")
