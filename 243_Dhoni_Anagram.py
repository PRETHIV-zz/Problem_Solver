#Dhoni sum
n=list("dhoni")
n.sort()
s=list(input())
s.sort()
c=0
for i in range(len(s)):
    if n[i]==s[i]:
        c+=1
    else:
        break
if c==len(s):
    print("yes")
else:
    print("no")
