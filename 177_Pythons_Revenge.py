#DS_Kathukrom_Mas_Pandrom
n,m=map(int,input().split())
a=list(map(int,input().split()))
na=[]
ma=[]
for i in range(n):
    na.append(a[i])
for i in range(n,m+n):
    ma.append(a[i])
nna=set(na)
mma=set(ma)
#print(nna)
#rint(mma)

c=nna.intersection(mma)

cl=list(c)
#print(cl)
for i in range(len(cl)):
    if i==len(cl)-1:
        print(cl[i],end="")
    else:
        print(cl[i],end=" ")
