#guvi hlo
def ispr(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n+1):
            if i==n:
                return True
            elif n%i==0:
                return False
n=int(input())
l=[]
for i in range(2,n+1):
    if n%i==0:
        if ispr(i):
            l.append(i)
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i],end="")
    else:
        print(l[i],end=" ")
