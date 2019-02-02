#6digitfloat
n=int(input())
s=0
for i in range(n):
    t=sum(list(map(int,input().split())))
    s+=t
print("{0:.6f}".format(s/(n*n)))
