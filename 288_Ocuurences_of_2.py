# your code goes here
def chk2(no):
    no=list(str(no))
    l=[i for i in no if i=='2']
    return len(l)
n=int(input())
ans=0
for i in range(1,n+1):
    ans+=chk2(i)
print(ans)
