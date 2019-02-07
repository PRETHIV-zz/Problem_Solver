#bihnary no
def deceq(n):
    su=0
    for i in range(n):
        su+=(2**i)
    return su
def makeq(s,c):
    while len(s)<c:
        s='0'+s
    return s
n=int(input())
decno=deceq(n)
#print(decno)
ans=[]
for i in range(decno+1):
    s=bin(i)
    s=s[2:]
    if len(s)==n:
        ans.append(s)
    else:
        ans.append(makeq(s,n))
for i in ans:
    print(i)
