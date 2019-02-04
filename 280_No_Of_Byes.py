n=int(input())
ans=1
c=0
while True:
    ans*=2
    if ans>=n:
        c=ans-n
        break
print(c)
