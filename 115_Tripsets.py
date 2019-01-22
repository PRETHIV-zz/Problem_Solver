n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l[i]<l[j]<l[k]:
                ll=[l[i],l[j],l[k]]
                ans.append(ll)
print(len(ans))
