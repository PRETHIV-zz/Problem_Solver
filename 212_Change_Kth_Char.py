#change every k th char to yper
s,k=map(str,input().split())
k=int(k)
ans=""
for i in range(len(s)):
    if (i+1)%k==0:
        ans+=s[i].upper()
    else:
        ans+=s[i]
print(ans)
