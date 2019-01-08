#it is my own code
n=int(input())
ans=1
if n==0:
  ans=1
else:
  while n>=1:
    ans=ans*n
    n=n-1
print(ans)
