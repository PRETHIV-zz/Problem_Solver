# Hello World program in Python
n,m=map(int,input().split())
flag=0
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if j==m:
            flag=1
            break
    if flag==1:
        break
if flag==0:
    print("no")
else:
    print("yes")
