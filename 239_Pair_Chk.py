#FindPair
n,k=map(int,input().split())
a=list(map(int,input().split()))
flag=False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            flag=True
            break
if flag:
    print("yes")
else:
    print("no")
