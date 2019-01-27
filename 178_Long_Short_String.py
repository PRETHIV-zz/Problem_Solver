#sm
s,m=map(str,input().split())
a=""
b=""
if len(s)>len(m):
    for i in range(len(m)):
        a+=s[i]
        b+=m[i]
elif len(m)>len(s):
    for i in range(len(s)):
        a+=s[i]
        b+=m[i]
else:
    a=s
    b=m
print(a+b)
