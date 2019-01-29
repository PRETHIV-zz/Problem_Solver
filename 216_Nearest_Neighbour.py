#Ready to Hunt
def sortnum(n,r):
    s=str(n)
    a=[]
    ss=""
    for i in s:
        ss+=i+" "
    a=list(map(int,ss.split()))
    a.sort()
    if r==1:
        a.reverse()
    ans=""
    for i in a:
        ans+=str(i)
    return int(ans)
n=int(input())
sn=sortnum(n,1)
if sn==n:
    print("impossible")
else:
    for i in range(n+1,sn+1):
        si=sortnum(i,1)
        if si==sn:
            print(i)
            break
