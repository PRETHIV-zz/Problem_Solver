#hlo guvi i am pret
n,k=map(int,input().split())
ans=[]
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]<k:
        ans.append(a[i])
ans.sort()
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
