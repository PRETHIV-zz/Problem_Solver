#minusdivide
n,k=map(int,input().split())
c=0
on=n
while n>0:
    n=n-k
    c+=1
if on<k:
    c=0
print(c)
