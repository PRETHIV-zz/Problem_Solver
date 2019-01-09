# Hello World program in Python
s=input()
c=0
for i in s:
    if i.isalpha():
        continue
    elif i.isnumeric():
        continue
    elif i.isspace():
        continue
    else:
        c+=1
print(c)
