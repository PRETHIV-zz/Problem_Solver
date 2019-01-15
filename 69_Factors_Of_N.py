#guvi hlo buddy
n=int(input())
for i in range(1,n+1):
    if i==n:
        print(i,end="")
    elif n%i==0:
        print(i,end=" ")
