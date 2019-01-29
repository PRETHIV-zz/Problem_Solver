#Be a pro
ans=[]
def findminrem(a,k):
    if k==0:
        return
    else:
        for i in a:
            s=str(i)
            na=[]
            for j in range(len(s)):
                val=s[0:j]+s[j+1:]
                ans.append(int(val))
                na.append(int(val))
        findminrem(na,k-1)
n,k=map(int,input().split())
ans.append(n)
findminrem([n],k)
print(min(ans))
