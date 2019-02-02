#JUMPING NUMBER FOUUND
def isjumpingno(n):
    s=str(n)
    cc=0
    for i in range(len(s)):
        if i==0:
            if abs(int(s[i])-int(s[i+1]))==1:
                cc+=1
        elif i==len(s)-1:
            if abs(int(s[i])-int(s[i-1]))==1:
                cc+=1
        else:
            if abs(int(s[i])-int(s[i+1]))==1 and abs(int(s[i])-int(s[i-1]))==1:
                cc+=1
    if cc==len(s):
        return True
    else:
        return False
n=int(input())
c=0
while n>=0:
    if n>9:
        if isjumpingno(n):
            c+=1
    else:
        c+=1
    n-=1
print(c)
