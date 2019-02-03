#Coin_Again
n,money=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
c.reverse()
cnt=0
while money!=0:
    for j in range(len(c)):
        if money>=c[j]:
            money-=c[j]
            break
    cnt+=1
print(cnt)
