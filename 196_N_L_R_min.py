#prethiv n l r min
n,l,r=map(int,input().split())
a=list(map(int,input().split()))
l-=1
m=a[l]
for i in range(l,r):
    if a[i]<m:
        m=a[i]
print(m)
