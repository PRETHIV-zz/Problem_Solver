#ai+aj=ak
n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if a[i]+a[j]==a[k] and k!=j and k!=i:
                print(a[i],a[j],a[k])
