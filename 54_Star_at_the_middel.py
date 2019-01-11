# Hello World program in Python
#guvi this is rocky
#rockys aim is getting output without using a single variable
a=input()
l=len(a)
ans=""
if l%2==1:
    l=l//2
    l=l+1
    for i in range(len(a)):
        if i+1==l:
            ans+="*"
        else:
            ans+=a[i]
else:
    l=l//2
    for i in range(len(a)):
        if i+1==l:
            ans+="**"
        else:
            ans+=a[i]
print(ans)
