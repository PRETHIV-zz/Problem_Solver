#prethiv.n
n=input()
l=list(map(str,n.split("0")))
l[len(l)-1]=0
for i in range(len(l)-1):
    if i==len(l)-2:
        s=l[i]
        for j in range(len(s)):
            if j==len(s)-1:
                print(s[j],end="")
            else:
                print(s[j],end=" ")
    else:
        s=l[i]
        for j in range(len(s)):
            print(s[j],end=" ")
