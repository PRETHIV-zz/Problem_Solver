#smallestandlargestindices
n=int(input())
a=list(map(int,input().split()))
m1=min(a)
m2=max(a)
ans=[]
for i in range(len(a)):
    if a[i]==m1:
        ans.append(i+1)
        break
for j in range(len(a)):
    if a[j]==m2:
        ans.append(j+1)
        break
print(*ans)
