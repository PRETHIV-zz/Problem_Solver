# Hello World program in Python
#guvi this is rocky
#rockys aim is getting output without using a single variable
def isprime(n):
    if n==1 or n==0:
        return False
    else:
        for i in range(2,n+1):
            if i==n:
                return True
            elif n%i==0:
                return False
print("yes" if isprime(int(input())) else "no")
