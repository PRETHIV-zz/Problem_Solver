#longest substring not a palin
def ispalin(s):
    s1=s[::-1]
    if s==s1:
        return True
    else:
        return False
n=input()
m=0
ans=""
for i in range(len(n)):
    s=n[i:]
    if not ispalin(s):
        if len(s)>m:
            m=len(s)
            ans=s
for i in range(len(n)-1,-1,-1):
    s=n[i::-1]
    #print("****")
    #print(s)
    s=s[::-1]
    if not ispalin(s):
        if len(s)>=m:
            m=len(s)
            ans=s
print(ans)
