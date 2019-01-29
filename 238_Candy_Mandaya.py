#Candy sum
n=int(input())
a=list(map(int,input().split()))
c=1
cc=1
for i in range(1,n):
    if a[i]>a[i-1]:
        cc+=1
        c=c+cc
    else:
        cc=1
        c=c+cc
print(c)
