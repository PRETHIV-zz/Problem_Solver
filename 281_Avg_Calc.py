#Equal avg finding
n=int(input())
a=list(map(int,input().split()))
find=False
for i in range(1,len(a)):
    l=a[0:i]
    r=a[i:]
    a1=sum(l)//len(l)
    a2=sum(r)//len(r)
    #print(l)
    #print(r)
    if a1==a2:
        #print(l)
        #print(r)
        find=True
        break
if find:
    print("yes")
else:
    print("no")
