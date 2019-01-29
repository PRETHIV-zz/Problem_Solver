#Increasing subarray recursion
def coutincr(a,i):
    l=i+1
    m=len(a)
    if l==m:
        return 1
    else:
        if a[i]<a[l]:
            return 1+coutincr(a,i+1)
        else:
            return 1
n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(len(a)):
    val=coutincr(a,i)
    if val>m:
        m=val
print(m)
