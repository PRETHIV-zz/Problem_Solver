def ispr(n):
    if n==0 or n==1:
        return False
    else:
        if n==2:
            return True
        else:
            for i in range(2,n,1):
                if i==n-1:
                    return True
                elif n%i==0:
                    return False
print("no" if ispr(int(input())) else "yes")
