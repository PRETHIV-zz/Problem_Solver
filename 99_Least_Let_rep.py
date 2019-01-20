#Mr.360
s=input()
f=[]
for i in s:
    c=-1
    for j in s:
        if ord(i)==ord(j) or abs(ord(i)-ord(j))==32:
            c+=1
    f.append(c)
m=min(f)
ans=[]
for i in range(len(f)):
    if m==f[i] and not s[i].isspace():
        ans.append(s[i])
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=" ")
