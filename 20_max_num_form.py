#guvi this is rocky
n=int(input())
l=list(map(int,input().split(" ")))
l.sort()
l.reverse()
s=""
for i in l:
    s=s+str(i)
ans=int(s)
print(s)
