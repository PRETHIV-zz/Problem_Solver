#hlo guvi i am pret
n=int(input())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=list(a.intersection(b))
c.sort()
for i in range(len(c)):
    if i==len(c)-1:
        print(c[i],end="")
    else:
        print(c[i],end=" ")
