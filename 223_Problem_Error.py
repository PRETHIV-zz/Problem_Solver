#Ready to Hunt
s=list(map(str,input().split()))
ans=""
for i in range(len(s)):
    if i==len(s)-1:
        ans+=s[i]
    else:
        ans+=s[i]+" "
print(ans)
