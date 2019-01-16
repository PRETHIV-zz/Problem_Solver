#include dayfinder.h nahi nahi Cyclic rotate
n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=l.copy()
for i in range(len(l)):
    l1[(i+k)%n]=l[i]
for i in range(len(l1)):
    if i==len(l1)-1:
        print(l1[i],end="")
    else:
        print(l1[i],end=" ")
