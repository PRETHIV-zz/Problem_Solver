#include dayfinder.h nahi nahi Cyclic rotate
n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=l.copy()
for i in range(len(l)):
    l1[(i+k)%n]=l[i]
print(l1)
