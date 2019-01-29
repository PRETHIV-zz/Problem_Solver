#Be apro
def bincount(no):
    s=bin(no)
    s=s[2:]
    c=0
    for i in s:
        if i=="1":
            c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
l=[]
ans=[]
for i in a:
    l.append(bincount(i))
m=max(l)
lt=min(l)
while m>=lt:
    t=[]
    for i in range(len(l)):
        if l[i]==m:
            t.append(a[i])
    t.sort()
    t.reverse()
    for i in t:
        ans.append(i)
    m-=1
for i in ans:
    print(i)
