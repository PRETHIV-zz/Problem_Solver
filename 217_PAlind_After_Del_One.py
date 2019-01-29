#Ready to Hunt
def ispalin(s):
    ss=s[::-1]
    if s==ss:
        return True
    else:
        return False
s=input()
ans=[]
c=0
for i in range(len(s)):
    a=""
    for j in range(len(s)):
        if i!=j:
            a+=s[j]
    ans.append(a)
for i in ans:
    if ispalin(i):
        print("YES")
        c+=1
        break
if c==0:
    print("NO")
