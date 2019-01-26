#hi guvi
n=int(input())
a=list(map(int,input().split()))
ans=[]
def pretmax(n1,n2):
    if n1>n2:
        return n1
    elif n2>n1:
        return n2
    else:
        return n1
for i in range(0,n-1,1):
    t=pretmax(a[i],a[i+1])
    ans.append(t)
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
