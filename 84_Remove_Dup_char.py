#guvist(s.copy())
s=input()
l=list(set(s))
d=list(s)
ans=""
for i in l:
    c=0
    for j in range(len(d)):
        if i==d[j] and c==0:
            c+=1
        elif i==d[j] and c==1:
            d[j]="#"
for i in d:
    if i!="#":
        ans+=i
print(ans)
