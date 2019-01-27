#hlo guvi
s=list(map(str,input().split()))
f=input()
l=[i+1 for i in range(len(s)) if s[i]==f]
print(l[0])
