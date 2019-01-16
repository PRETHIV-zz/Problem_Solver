#include fun.h
s=input()
s1=list(set(s))
s2=[0]*len(s1)
for i in range(len(s1)):
    c=0
    for j in s:
        if s1[i]==j:
            c+=1
    s2[i]=c
m=max(s2)
for i in range(len(s2)):
    if s2[i]==m:
        print(s1[i])
