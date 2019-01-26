#dec2bin
n=input()
n=n[::-1]
ans=0
c=0
for i in n:
    ans=ans+int(i)*(2**c)
    c+=1
a=hex(ans)
print(a[2:])
