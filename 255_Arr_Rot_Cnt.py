#ArrayRotationcount
n=int(input())
a=list(map(int,input().split()))
ra=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
    for j in range(n):
        ans[j]=a[(j+i)%n]
    if ans==ra:
        print(i)
        break
