#it is my own code guvi
n=int(input())
on=n
dig=0
l=[]
while on>0:
    dig=dig+1
    l.append(on%10)
    on=on//10
res=0
for i in l:
    res=res+(i**dig)
if res==n:
    print("yes")
else:
    print("no")
