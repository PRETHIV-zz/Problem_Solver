#letter_upr
s=input()
c=1
ans=""
for i in s:
    if i.isspace():
        ans+=i
        continue
    else:
        if c%2==1:
            ans+=i.upper()
        else:
            ans+=i
        c+=1
print(ans)
