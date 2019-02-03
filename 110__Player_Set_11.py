#Murder_Case
n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(1,len(a)):
    for j in range(i):
        if a[j]<a[i]:
            ans.append(a[j])
print(sum(ans))
