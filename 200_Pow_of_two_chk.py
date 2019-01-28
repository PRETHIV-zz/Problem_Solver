#prethiv n l r min
n=int(input())
on=n
c=0
while on>0:
    on=on//2
    c+=1
c-=1
if (2**c)==n:
    print("yes")
else:
    print("no")
