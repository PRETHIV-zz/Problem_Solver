#prethiv n l r min
s=list(map(str,input().split()))
ss=s.copy()
for i in range(0,len(ss)):
    if i!=0 and i!=len(ss)-1:
        v=s[i][::-1]
        ss[i]=v
for i in range(len(ss)):
    if i==len(ss)-1:
        print(ss[i],end="")
    else:
        print(ss[i],end=" ")
