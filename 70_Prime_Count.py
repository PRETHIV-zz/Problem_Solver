#include fun.h :-)
def ispr(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    else:
        for i in range(2,n):
            if i==n-1:
                return True
            elif n%i==0:
                return False
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    if ispr(i):
        c+=1
print(c)
