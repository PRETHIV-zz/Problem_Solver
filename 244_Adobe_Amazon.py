#Adobe_Amazon
n,p,q,r=map(int,input().split())
a=list(map(int,input().split()))
m=p*a[0]+q*a[0]+r*a[0]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<=j and j<=k:
                val=p*a[i]+q*a[j]+r*a[k]
                if val>m:
                    m=val
print(val)
