#guvi this is rocky
n=int(input())
l=list(map(int,input().split(" ")))
s=set(l)
s=sum(s)*2
ans=s-sum(l)
print(ans)
