#string in k
s,k=map(str,input().split())
k=int(k)
k-=1
ans=s[k::k+1]
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
