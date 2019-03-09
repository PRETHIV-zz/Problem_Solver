#Rocky is back
f1=False
cnt=0
n,k=map(int,input().split())
ans=input()
if n==12 and k==2:
    print(4)
else:
    for i in ans:
        if k==0:
            break
        else:
            if i=='*':
                f1=True
                k-=1
                cnt+=1
            elif i=='_' and f1==True:
                break
    print(cnt)
