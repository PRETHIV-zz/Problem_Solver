#hlo guvi it is pret
n=int(input())
f=0
for i in range(2,n):
    if n%i==0:
        f=1
        break
print("yes" if f==1 else "no")
