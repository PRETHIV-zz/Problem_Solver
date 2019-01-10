#guvi this is rocky
n=int(input())
l=list(map(int,input().split(" ")))
ans=[]
for i in range(len(l)):
    if i==l[i]:
        ans.append(i)
ans.sort()
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
