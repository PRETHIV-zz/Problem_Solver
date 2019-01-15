#guvi this is rocky
n,m=map(int,input().split())
l=[]
ans=[]
for i in range(n):
    lt=set(map(int,input().split()))
    l.append(lt)
a=l[0]
for i in range(1,n):
    a=a.intersection(l[i])
    ans.append(a)
b=list(ans[len(ans)-1])
for i in range(len(b)):
    if i==len(b)-1:
        print(b[i],end="")
    else:
        print(b[i],end=" ")
