#hlo guvi i am pret
n,k=map(int,input().split())
flag=0
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            flag=1
            break
if flag==1:
    print("yes")
else:
    print("no")
