#prethiv n l r min
def factpret(n):
    if n==0:
        return 1
    else:
        return n*factpret(n-1)
a,b=map(int,input().split())
print(factpret(a)//factpret(b))
