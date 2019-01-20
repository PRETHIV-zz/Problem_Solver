#morning_Python_7.30AM_20/01/2019
def chksqr(n):
    s=n**(1/2)
    s*=s
    if s==n:
        return True
    else:
        return False
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    if chksqr(i):
        c+=1
print(c)
