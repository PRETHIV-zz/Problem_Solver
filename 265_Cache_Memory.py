#LRU_Cache
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(k):
    ans.insert(0,a[i])
#print(ans)
for i in range(k,len(a)):
    if a[i] in ans:
        for j in range(len(ans)):
            if a[i]==ans[j]:
                ans[0],ans[j]=ans[j],ans[0]
                break
    else:
        ans.pop()
        ans.insert(0,a[i])
ans.reverse()
print(*ans)
