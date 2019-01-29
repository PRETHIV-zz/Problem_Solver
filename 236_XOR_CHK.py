#Xor_Find
n,q=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(q):
    u,v=map(int,input().split())
    val=a[u-1]
    for j in range(u,v):
        val^=a[j]
    ans.append(val)
for i in ans:
    print(i)
