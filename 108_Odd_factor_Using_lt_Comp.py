#hlo guvi
n=int(input())
l=[ i for i in range(1,n+1) if i%2==1 and n%i==0 ]
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i],end="")
    else:
        print(l[i],end=" ")
