#hi guvi i am rocky from home towny
n=int(input())
l=list(map(int,input().split(" ")))
ans=[]
for i in range(len(l)):
    if i%2==0 and l[i]%2==1:
        ans.append(l[i])
    elif i%2==1 and l[i]%2==0:
        ans.append(l[i])
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end=" ")
    else:
        print(ans[i],end=" ")
