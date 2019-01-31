# your code goes here
ans=[]
def mularr(a):
    aa=1
    for i in a:
        aa=aa*i
    ans.append(aa)
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
	ar=a[i:]
	mularr(ar)
a.reverse()
for i in range(len(a)):
	ar=a[i:]
	mularr(ar)
print(max(ans))
