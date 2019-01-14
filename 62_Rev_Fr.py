#guvi this is rocky
s=[]
str1=list(map(str,input().split(" ")))
def revfr(os):
    ans=""
    for i in os:
        ans=i+ans
    s.append(ans)
for i in str1:
    revfr(i)
for i in range(len(s)):
    if i==len(s)-1:
        print(s[i],end="")
    else:
        print(s[i],end=" ")
