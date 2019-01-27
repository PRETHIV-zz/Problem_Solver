#Hlo guvi
n,q=map(int,input().split("_"))
a=list(map(int,input().split()))
ans=[]
for i in range(q):
    s,e=map(int,input().split())
    sumi=-1
    ans.append(sumi)
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i])
