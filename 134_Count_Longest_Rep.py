#hlo guvi i am pret
n=int(input())
a=list(map(int,input().split()))
lt=[]
def retlen(ar,i):
    l=i+1
    m=len(ar)-1
    if l>m:
        return 1
    else:
        if ar[i]==ar[l]:
            return 1+retlen(ar,i+1)
        else:
            return 1
for i in range(len(a)):
    n=retlen(a,i)
    lt.append(n)
print(max(lt))
