#hlo guvi i am pret
a,b=map(str,input().split())
a1=set(a)
a2=set(b)
a3=a1.intersection(a2)
if len(a3)>=1:
    print("yes")
else:
    print("no")
