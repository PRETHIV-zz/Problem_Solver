#guvi i am rocky
s=input()
class Node:
    def __init__(self,data):
        self.d=data
        self.nextval=None
h=Node(s[-1])
p=h
for i in range(len(s)-2,-1,-1):
    nn=Node(s[i])
    p.nextval=nn
    p=p.nextval
p=h
flag=0
#flag is 0 then palindrome else not
for i in s:
    if i!=p.d:
        flag=1
        break
    p=p.nextval
if flag==0:
    print("YES")
else:
    print("NO")
