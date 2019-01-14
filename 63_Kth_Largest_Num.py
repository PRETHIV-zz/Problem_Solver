#guvi this is ROCK$
n,k=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
s=min(l)
for i in range(k-1):
    m=max(l)
    for j in range(len(l)):
        if l[j]==m:
            l[j]=s
print(max(l))
