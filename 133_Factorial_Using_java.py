#hlo guvi i am pret
n=int(input())
ans=1
if n==0:
    print(ans)
else:
    while n>=1:
        ans*=n
        n-=1
    print(ans)
