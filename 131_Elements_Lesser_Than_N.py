#hlo guvi i am pret
n=int(input())
ans=[]
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]<n:
        ans.append(a[i])
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
