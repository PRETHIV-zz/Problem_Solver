#counting vowels
def vowpresent(s):
    vow=['a','e','i','o','u','A','E','I','O','U']
    c=0
    for i in s:
        if i in vow:
            c+=1
            break
    if c!=0:
        return True
    else:
        return False

c=0
n=int(input())
for i in range(n):
    s=input()
    if vowpresent(s):
        c+=1
if c==n:
    print("yes",end="")
else:
    print("no",end="")
