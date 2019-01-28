#prethiv n l r min
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i==k:
        c+=1
if c==0:
    print("no")
else:
    print("yes",c)
