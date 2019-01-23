#prethiv.n
import sys
ans=[]
for line in sys.stdin:
    a,b=map(int,line.split())
    c=b-a
    ans.append(c)
for i in range(len(ans)):
    print(ans[i])
