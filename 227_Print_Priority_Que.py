#Ready to Hunt
n=int(input())
a=list(map(int,input().split()))
ans=[a[0]]
m=a[0]
for i in range(1,n):
    if a[i]<=m:
        ans.append(a[i])
        m=a[i]
    else:
        ans.append(m)
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
