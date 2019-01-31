#alternating ab str
def abcount(s,i):
    l=i+1
    if l==len(s):
        return 1
    else:
        if s[i]=='a' and s[l]=='b':
            return 1+abcount(s,l)
        if s[i]=='b' and s[l]=='a':
            return 1+abcount(s,l)
        else:
            return 1
n=input()
ans=[]
for i in range(len(n)-1):
    if n[i]=='a' and n[i+1]=='b':
        ans.append(abcount(n,i))
if len(ans)==0:
    print(0)
else:
    print(max(ans))
