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
lim=n
if n%2==1:
    lim=n-1
for i in range(0,lim,2):
    t=pretmax(a[i],a[i+1])
    ans.append(t)
if n%2==1:
    ans.append(a[n-1])
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
