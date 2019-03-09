#REV_EVERY_WORDS
s=input()
ans=""
l=[]
l=list(map(str,s.split()))
for i in l:
    t=list(i)
    t.reverse()
    for j in t:
        ans+=j
    ans+=" "
print(ans[0:len(ans)-1])
