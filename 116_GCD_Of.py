#GCD Of 2 nos
n,q=map(int,input().split())
lt=list(map(int,input().split()))
l=[]
r=[]
ans=[]
for i in range(q):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
for i in range(q):
    a=l[i]
    b=r[i]
    if a==b:
        ans.append(lt[a-1])
    else:
        chk=[]
        for j in range(a-1,b):
            chk.append(lt[j])
        gcd=1
        lim=max(chk)
        lchk=len(chk)
        for k in range(1,lim+1):
            c=0
            for kk in range(len(chk)):
                if chk[kk]%k==0:
                    c+=1
            if c==lchk and k>=gcd:
                gcd=k
        ans.append(gcd)
for i in ans:
    print(i)
