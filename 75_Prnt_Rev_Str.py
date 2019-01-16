#rem vow and print rev
n=int(input())
s=input()
v=['a','e','i','o','u','A','E','I','O','U']
sr=""
for i in s:
    f=0
    for j in v:
        if i==j:
            f=1
            break
    if f==0:
        sr=sr+i
ans=""
for i in sr:
    ans=i+ans
print(ans)
