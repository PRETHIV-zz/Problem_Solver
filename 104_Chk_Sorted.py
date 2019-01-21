# Hello World program in Python
n=int(input())
s=list(map(int,input().split()))
ss=s.copy()
s.sort()
i=0
for j in range(len(s)):
    if s[i]==ss[i]:
        i+=1
if i==len(s):
    print("yes")
else:
    print("no")
