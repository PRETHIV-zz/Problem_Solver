#min dist u v
n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        a1=a[j]-a[i]
        ans.append(a1)
print(max(ans))
