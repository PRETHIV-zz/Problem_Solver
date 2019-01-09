#guvi this is rocky
s=input()
ans=""
for i in range(0,len(s)-1,2):
    ans=ans+s[i+1]
    ans=ans+s[i]
print(ans)
