#prethiv n l r min
n=int(input())
l=0
m=(n//2)
r=n
a=list(map(int,input().split()))
la=[a[i] for i in range(l,m)]
ra=[a[i] for i in range(m,r)]
la.sort()
ra.sort()
ra.reverse()
ans=la
ans.extend(ra)
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
