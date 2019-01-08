n=int(input())
rev=0
a=n
while n>0:
    rev=10*rev+(n%10)
    n=n//10
if rev==a:
    print("yes")
else:
    print("no")
