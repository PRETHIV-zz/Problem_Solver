#Python Hater
s=list(map(str,input().split()))
ans=[]
for i in range(len(s)):
    if i%2==0:
        t=s[i]
        t=t[::-1]
        ans.append(t)
    else:
        ans.append(s[i])
print(*ans)
