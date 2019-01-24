#hlo guvi i am pret
import sys
ans=[]
for line in sys.stdin:
    a=list(map(str,line.split()))
    n1=int(a[0])
    s=a[1]
    n2=int(a[2])
    if s=="%":
        c=n1%n2
        ans.append(c)
    elif s=="/":
        c=n1//n2
        ans.append(c)
for i in range(len(ans)):
    print(ans[i])
