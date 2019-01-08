#it is my own code guvi
ans=[]
def chkarm(n):
    on=n
    dig=0
    l=[]
    while on>0:
        dig=dig+1
        l.append(on%10)
        on=on//10
    res=0
    for i in l:
        res=res+(i**dig)
    if res==n:
        ans.append(res)
l1,l2=map(int,input().split(" "))
for i in range(l1+1,l2):
    chkarm(i)
for i in range(len(ans)):
    if i==(len(ans)-1):
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
