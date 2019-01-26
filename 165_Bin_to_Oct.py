#dec2bin
n=input()
n=n[::-1]
ans=0
c=0
for i in n:
    ans+=int(i)*(2**c)
    c+=1
a=oct(ans)
print(a[2:])
