#Merse and sort
k=int(input())
ans=[]
for i in range(k):
    a=list(map(int,input().split()))
    ans+=a
ans.sort()
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
