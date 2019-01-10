#hlo guvi
n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
ans=[]
for i in s:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c!=1:
        ans.append(i)
ans.sort()
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
