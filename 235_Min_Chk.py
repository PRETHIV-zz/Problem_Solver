#Minimum value of array indices
n,q=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(q):
    u,v=map(int,input().split())
    u=u-1
    t=[]
    for j in range(u,v):
        t.append(a[j])
    ans.append(min(t))
for i in ans:
    print(i)
