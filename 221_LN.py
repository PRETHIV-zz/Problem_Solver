#Ready to Hunt
n=int(input())
a=list(map(int,input().split()))
m=max(a)
c=0
for i in range(1,m+1):
    aa=i*n
    if aa>m:
        break
    for j in a:
        if j==aa:
            c+=1
print(c)
