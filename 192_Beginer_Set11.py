#Hlo guvi
n,q=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(q):
    s,e=map(int,input().split())
    s=s-1
    e=e-1
    sumi=0
    for j in range(s,e+1):
        sumi+=a[j]
    ans.append(sumi)
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i])
