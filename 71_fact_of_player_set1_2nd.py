# include factorial.h
n=int(input())
ans=1
if n==0:
  print(ans)
else:
  while n>0:
    ans*=n
    n-=1
  print(ans)
