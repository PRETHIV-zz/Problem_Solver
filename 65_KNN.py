#guvi hlo its 5:55 i am in my home town still love to code:-))
n,k=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
ans=[]
a=[]
for i in l:
    a.append(abs(i-k))
m=max(a)
c=0
for i in range(len(a)):
    if a[i]==0:
        a[i]=m
flag=0
for i in range(3):
    s=min(a)
    for j in range(len(a)):
        if s==a[j]:
            c+=1
            a[j]=m
            ans.append(l[j])
        if c==3:
            flag=1
            break
    if flag==1:
        break
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
