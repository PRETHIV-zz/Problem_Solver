#min dist u v
def findgreat(ar):
    m=ar[0]
    for i in ar:
        if i>m:
            m=i
    return m
n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(len(a)-1):
    d=a[i+1:]
    #print(d)
    #print(max(d))
    ans.append(max(d))
ans.append(0)
print(*ans,end="")
