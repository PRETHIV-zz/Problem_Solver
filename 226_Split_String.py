#Ready to Hunt
s,k=map(str,input().split())
k=int(k)
ans=[]
for i in range(len(s)):
    a=s[i:i+k]
    if len(a)==k:
        ans.append(a)
for i in range(len(ans)):
    if i==len(ans):
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
