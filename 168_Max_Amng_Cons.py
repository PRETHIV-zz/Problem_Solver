n=int(input())
a=list(map(int,input().split()))
ad=[]
for i in range(len(a)):
    s=0
    for j in range(i+1,len(a)):
        s=s+a[j]
    ad.append(s)
print(max(ad))
