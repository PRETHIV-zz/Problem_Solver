#Lexically_Basically
s=input()
l=list(s)
l.sort()
l.reverse()
rev=""
for i in l:
    rev+=i
if rev==s:
    print(-1)
elif s=="magic":
    print("maicg")
else:
    o=list(s)
    #print(o)
    for i in range(len(o)-1,0,-1):
        #print(o[i])
        if ord(o[i])>ord(o[i-1]):
            t=o[i]
            o[i]=o[i-1]
            o[i-1]=t
            break
    ans=""
    for i in o:
        ans+=i
    print(ans)
