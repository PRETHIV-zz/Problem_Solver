#Bin Prime
def ispri(n):
    if n<2:
        return False
    else:
        for i in range(2,n+1):
            if i==n:
                return True
            elif n%i==0:
                return False
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    s=bin(i)
    s=s[2:]
    o=0
    for j in s:
        if j=="1":
            o+=1
    if ispri(o):
        c+=1
print(c)
