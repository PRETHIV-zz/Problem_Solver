#letterencode
s=input()
cmp=s[0]
i=0
ans=[]
t=0
while i<len(s):
    if cmp==s[i]:
        t+=1
    else:
        ans.append(t)
        t=1
        cmp=s[i]
    i+=1
ans.append(t)
h=0
ind=[]
asp=""
for i in ans:
    h+=i
    ind.append(h)
for i in range(len(ind)):
    if ans[i]==1:
        asp=asp+s[ind[i]-1]
    else:
        asp+=str(ans[i])+"*"+s[ind[i]-1]
print(asp)
