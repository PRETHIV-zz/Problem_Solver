#asec desc
n,k=map(int,input().split())
a=list(map(int,input().split()))
la=a[0:k]
ra=a[k:len(a)]
la.sort()
ra.sort()
ra.reverse()
ans=la+ra
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
