# Hello World program in Python
#guvi this is rocky
n,k=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
c=0
for i in a:
    if i==k:
        c+=1
        break
print("yes" if c==1 else "no")
